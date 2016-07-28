from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from decimal import Decimal

from django.conf import settings
from audiofield.fields import AudioField
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from geopy.geocoders import Nominatim
from geopy.distance import vincenty, great_circle

from friendship.models import Friend, Follow, FriendshipRequest
from projects.forms import ProjectForm, ProjectEditForm, UploadProjectForm1, UploadProjectForm2
from projects.models import Project, ProjectMatch
from profiles.models import Profile
from tribe.models import TribeAudioProject, TribeComment
from tribe.forms import TribeCommentForm



User = get_user_model()



@login_required
def project_list(request):
	page_title = "My Projects"
	projects = Project.objects.filter(user=request.user).order_by('-timestamp')
	projects_count = Project.objects.filter(user=request.user).count

	context = {
		'projects': projects,
		'page_title': page_title,
		}

	return render(request, 'projects.html', context)




@login_required
def project_create(request):
	status = 200
	page_title = "Upload Project"
	friends = Friend.objects.friends(request.user)
	total_match_projects = Project.objects.filter(user=request.user).count()
	matches = []

	if request.user.is_authenticated() and total_match_projects < 6:
		form = ProjectForm()

		if request.method == 'POST':
			form = ProjectForm(request.POST, request.FILES)
			latitude = request.POST.get('lat')
			longitude = request.POST.get('lng')
			print latitude, longitude
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.latitude = latitude
				instance.longitude = longitude
				instance_genre = form.cleaned_data.get('genre')
				instance_title = form.cleaned_data.get('title')
				instance_nearby = form.cleaned_data.get('match_nearby')
				instance_queued = form.cleaned_data.get('queued')
				instance.save()

				if instance_queued == True:

					print ("Searching for a Match")


					if Project.objects.filter(queued=True, genre=instance_genre).exclude(user=instance.user).exclude(user__in=friends).exists():

						print ("Potential Matches Found")


						queued_projects = Project.objects.filter(queued=True, genre=instance_genre).exclude(user=instance.user).exclude(user__in=friends)

						print queued_projects



						for project in queued_projects:

							print project.user, project.title

							user_a = request.user
							user_b = project.user
							project_a = Project.objects.get(title=instance_title)
							project_b = Project.objects.get(id=project.id)


							user_a_latitude = latitude
							user_a_longitude = longitude
							user_a_location = (user_a_latitude, user_a_longitude)
							print user_a_location

							user_b_latitude = project.latitude
							user_b_longitude = project.longitude
							user_b_location = (user_b_latitude, user_b_longitude)
							print user_b_location

							distance = (vincenty(user_a_location, user_b_location).miles)
							print distance


							if instance_nearby == True and distance < 30:

								print ('User A is Nearby', project.user)

								items_wanted = project
								matches.append(items_wanted)
									


							elif project.match_nearby == True and distance < 30:

								print ('User B is Nearby', project.user)

								items_wanted = project
								matches.append(items_wanted)



							elif instance_nearby == False and project.match_nearby == False:

								print ('Neither Local Only', project.user)

								items_wanted = project
								matches.append(items_wanted)

							

						if matches:

							print ('Found A Match')

							print matches

							match = matches[0]

							print match
							print match.user
							
							ProjectMatch.objects.create(user_a=user_a, user_b=match.user, project_a=project_a, project_b=match)
							
							instance.queued = False
							instance.save()
							match.queued = False
							match.save()
							
							instance.matched_users.add(match.user)
							match.matched_users.add(user_a)


							return redirect ("home")


						else:

							print ('No Location Matches')
							return redirect ("home")


					else:
						print ('No Genre Matches')
						return redirect ("home")
				

				else:
					print ('Match Not Desired')
					return redirect("get_project", id=instance.id)

			else:

				status = 422 # signal error to UploadProgress

		context = {
		'form': form,
		'page_title': page_title,
		}

		return render(request, 'upload_project.html', context, status=status)


	else:

		return redirect ("upload_project_limit")







@login_required
def project_detail(request, id):
	user = request.user
	instance = get_object_or_404(Project, id=id)
	page_title = instance.title
	friends = Friend.objects.friends(instance.user)
	form = TribeCommentForm()
	queueable = True
	unfed_session = None
	matches = []

	
	if request.user == instance.user or request.user in friends:


		project_a_session = ProjectMatch.objects.filter(project_a=instance).exclude(user_a_positive_feedback__isnull=True).exclude(user_a_negative_feedback__isnull=True).exclude(user_a_positive_feedback__exact='').exclude(user_a_negative_feedback__exact='').order_by('-timestamp')
		project_b_session = ProjectMatch.objects.filter(project_b=instance).exclude(user_b_positive_feedback__isnull=True).exclude(user_b_negative_feedback__isnull=True).exclude(user_b_positive_feedback__exact='').exclude(user_b_negative_feedback__exact='').order_by('-timestamp')
		feedback = (project_a_session | project_b_session).distinct()



	if request.user == instance.user:

		project_a_fed = ProjectMatch.objects.filter(project_a=instance, active=True, user_b_positive_feedback__exact='', user_b_negative_feedback__exact='').order_by('timestamp')
		project_b_fed = ProjectMatch.objects.filter(project_b=instance, active=True, user_a_positive_feedback__exact='', user_a_negative_feedback__exact='').order_by('timestamp')
		unfed = (project_a_fed | project_b_fed).distinct()

		print (unfed)

		if not unfed:
			print ("Read to queue")

			queueable = True

		else:
			print ("Still need to give feedback")

			queueable = False

			unfed_session = unfed[0]

			print (unfed_session)



		comments = TribeComment.objects.filter(project=instance).order_by('timestamp')


		if 'give_feedback' in request.POST:

			form = TribeCommentForm(request.POST or None)
			
			if form.is_valid():
				comment_instance = form.save(commit=False)
				comment_instance.user = request.user
				comment_instance.project = instance
				comment_instance.project_user = instance.user
				comment_instance.save()

				return redirect("get_project", id=instance.id)


		if 'deactivate' in request.POST:

			print ("Deactivate")

			instance.active = False
			instance.queued = False
			instance.save()
			return redirect("get_project", id=instance.id)


		if 'activate' in request.POST:

			print ("Activate")

			instance.active = True
			instance.save()
			return redirect("get_project", id=instance.id)


		if 'leave_queue' in request.POST:

			instance.queued = False
			instance.save()
			return redirect("get_project", id=instance.id)


		if 'get_matched' in request.POST:


			if Project.objects.filter(queued=True, genre=instance.genre).exclude(user=instance.user).exclude(user__in=friends).exists():

				queued_projects = Project.objects.filter(queued=True, genre=instance.genre).exclude(user=instance.user).exclude(user__in=friends)

				print queued_projects

				for project in queued_projects:

					print project.user, project.title

					user_b = project.user
					project_b = project

					user_a_latitude = instance.latitude
					user_a_longitude = instance.longitude
					user_a_location = (user_a_latitude, user_a_longitude)
					print user_a_location

					user_b_latitude = project.latitude
					user_b_longitude = project.longitude
					user_b_location = (user_b_latitude, user_b_longitude)
					print user_b_location

					distance = (vincenty(user_a_location, user_b_location).miles)
					print distance


					if instance.match_nearby == True and distance < 30 and not user_b in instance.matched_users.all():

						print ('User A is Nearby', project.user)

						items_wanted = project
						matches.append(items_wanted)
								

					elif project.match_nearby == True and distance < 30 and not user_b in instance.matched_users.all():

						print ('User B is Nearby', project.user)

						items_wanted = project
						matches.append(items_wanted)


					elif instance.match_nearby == False and project.match_nearby == False and not user_b in instance.matched_users.all():

						print ('Neither Local Only', project.user)

						items_wanted = project
						matches.append(items_wanted)


				if matches:

					print ('Found A Match')

					print matches

					match = matches[0]

					print match
					print match.user
						
					ProjectMatch.objects.create(user_a=instance.user, user_b=match.user, project_a=instance, project_b=match)
						
					instance.queued = False
					instance.save()
					match.queued = False
					match.save()
						
					instance.matched_users.add(match.user)
					match.matched_users.add(instance.user)

					return redirect ("home")


				else:

					print ('No Location Matches')

					instance.queued = True
					instance.save()
					return redirect ("home")


			else:

				print ('No Genre Matches')

				instance.queued = True
				instance.save()
				return redirect ("home")


		context = {
		'instance': instance,
		'project_a_session': project_a_session,
		'project_b_session': project_b_session,
		'feedback': feedback,
		'page_title': page_title,
		'form': form,
		'comments': comments,
		'queueable': queueable,
		'unfed_session': unfed_session,
		}

		return render(request, 'project.html', context)

	else:
		return HttpResponse(status=403)





@login_required
def edit_project(request, id):
	user = request.user
	page_title = "Edit Project"
	instance = get_object_or_404(Project, id=id)

	if request.user == instance.user:

		form = ProjectEditForm(request.POST or None, request.FILES or None, instance=instance)

		if form.is_valid():
		
			instance = form.save(commit=False)
			instance.save()

			return redirect("get_project", id=instance.id)



		context = {
		'instance': instance,
		'page_title': page_title,
		'form': form,
		}


		return render(request, 'project_edit.html', context)

	else:
		return HttpResponse(status=403)




@login_required
def delete_project(request, id):
	user = request.user
	page_title = "Delete Project"
	instance = get_object_or_404(Project, id=id)

	if request.user == instance.user:


		if 'delete' in request.POST:

			print ("Delete")

			instance.delete()
			return redirect ("projects")

		context = {
		'instance': instance,
		'page_title': page_title,
		}


		return render(request, 'project_delete.html', context)

	else:
		return HttpResponse(status=403)




@login_required
def upload_project_limit(request):
	page_title = "Project Limit Exceeded!"

	if request.user.is_authenticated():

		context = {
		'page_title': page_title,
		}


		return render(request, 'upload_project_limit.html', context)

	else:
		return HttpResponse(status=403)






















@login_required
def getfeedback(request):
	page_title = "Get Feedback"
	matched_projects = Project.objects.filter(user=request.user).order_by('-timestamp')
	matched_projects_count = Project.objects.filter(user=request.user).count
	tribe_projects = TribeAudioProject.objects.filter(user=request.user).order_by('-timestamp')
	total_feedbackers = Friend.objects.filter(to_user=request.user).count()
	display_tribe = True

	if total_feedbackers == 0:
		display_tribe = False



	# tribe_feedback = TribeComment.objects.filter(project_user=request.user, project= ).order_by('-timestamp')

	context = {
		'matched_projects': matched_projects,
		'tribe_projects': tribe_projects,
		'page_title': page_title,
		'display_tribe': display_tribe,
		'total_feedbackers': total_feedbackers,
		}

	return render(request, 'getfeedback.html', context)











