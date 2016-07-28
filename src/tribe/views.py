from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse

from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from embed_video.fields import EmbedVideoField

from friendship.models import Friend, Follow, FriendshipRequest
from profiles.models import Profile, Notification, MySubTribe, MySubTribeProject
from projects.models import Project
from tribe.models import TribeFeedItem, TribeAudioProject, TribeComment, TribeAudioInspiration
from .forms import SubTribeForm, SubTribeEditForm, SubTribeProjectForm, TribeCommentForm, TribeProjectForm, TribeAudioInspirationForm




# User = get_user_model()

User = settings.AUTH_USER_MODEL



@login_required
def get_tribe_feed(request):
	page_title = "BounceTribe"
	feed_items = []
	all_friends = Friend.objects.friends(request.user)
	tribe_feed_items = TribeFeedItem.objects.all().order_by('-timestamp')
	
	total_feedbackers = Friend.objects.filter(to_user=request.user).count()
	display_tribe = True

	if total_feedbackers == 0:
		display_tribe = False


	for item in tribe_feed_items:
		if item.user in all_friends or item.user == request.user:
			items_wanted = [item.user, item]
			feed_items.append(items_wanted)


	paginator = Paginator(feed_items, 5)

	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	
	except PageNotAnInteger:
		items = paginator.page(1)
	
	except EmptyPage:
		items = paginator.page(paginator.num_pages)



	context = {
		'page_title': page_title,
		'display_tribe': display_tribe,
		'all_friends': all_friends,
		'feed_items': feed_items[:10],
		'items': items,
		}

	return render(request, 'tribe_feed.html', context)




@login_required
def audio_inspiration_create(request):
	page_title = "Share Inspiration"

	if request.user.is_authenticated():
		form = TribeAudioInspirationForm()

		if request.method == 'POST':
			form = TribeAudioInspirationForm(request.POST, request.FILES)
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.save()

				return redirect ("tribe_feed")


		context = {
		'form': form,
		'page_title': page_title,
		}

		return render(request, 'tribe_audio_inspiration.html', context)



@login_required
def audio_inspiration_delete(request, id):
	page_title = "Delete Inspiration"
	instance = get_object_or_404(TribeFeedItem, id=id)

	if request.user == instance.user:

		if 'delete' in request.POST:

			instance.delete()
			return redirect ("tribe_feed")

	
		context = {
		'instance': instance,
		'page_title': page_title,
		}

		return render(request, 'tribe_audio_inspiration_delete.html', context)

	else:
		return HttpResponse(status=403)





@login_required
def subtribe(request, id):
	user = request.user.profile.name
	instance = get_object_or_404(MySubTribe, id=id)
	profile_name = Profile.objects.get(user=request.user)
	page_title = instance.name
	leader = instance.leader
	members = instance.members.all()
	member_check = MySubTribe.objects.filter(id=id, members=profile_name)
	friends = Friend.objects.friends(request.user)

	projects = MySubTribeProject.objects.filter(subtribe=instance)


	if request.user == instance.leader or member_check:


		context = {
		'instance': instance,
		'page_title': page_title,
		'members': members,
		'leader': leader,
		'profile_name': profile_name,
		'user': user,
		'member_check': member_check,
		'projects': projects,
		}
		return render(request, 'subtribe.html', context)


	else:
		return HttpResponse(status=403)



@login_required
def subtribe_create(request):
	page_title = 'Create SubTribe'
	friends = Friend.objects.friends(request.user)

	if request.user.is_authenticated():
		form = SubTribeForm(request.POST or None)
		form.fields["members"].queryset = Profile.objects.filter(user__in=friends)


		if request.method == 'POST':
			
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.leader = request.user
				instance.save()
				form.save_m2m()

				members = instance.members.all()

				for member in members:

					Notification.objects.create(user=member.user, from_user=instance.leader, notification_type="SubTribe Created", title="SubTribe Created!", text="has added you to their SubTribe.", subtribe=instance)


				return redirect("subtribe", id=instance.id)


		context = {
		'friends': friends,
		'page_title': page_title,
		'form': form,
		}
		return render(request, 'subtribe_create.html', context)





@login_required
def subtribe_leave(request, id):
	profile_name = Profile.objects.get(user=request.user)
	page_title = "Leave Subtribe"
	instance = get_object_or_404(MySubTribe, id=id)
	member_check = MySubTribe.objects.filter(id=id, members=profile_name)

	if member_check:

	
		if 'leave' in request.POST:

			instance.members.remove(profile_name)

			return redirect ("tribe")


		context = {
		'instance': instance,
		'page_title': page_title,
		}


		return render(request, 'subtribe_leave.html', context)

	else:
		return HttpResponse(status=403)




@login_required
def subtribe_edit(request, id):
	profile_name = Profile.objects.get(user=request.user)
	page_title = "Edit Subtribe"
	instance = get_object_or_404(MySubTribe, id=id)
	friends = Friend.objects.friends(request.user)
	original_members = instance.members.all()
	member_check = MySubTribe.objects.filter(id=id, members=profile_name)


	if request.user == instance.leader:

		print original_members

		form = SubTribeEditForm(request.POST or None, instance=instance)

		form.fields["members"].queryset = Profile.objects.filter(user__in=friends)


		if request.method == 'POST':
			
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				form.save_m2m()


				return redirect("subtribe", id=instance.id)



		context = {
		'instance': instance,
		'page_title': page_title,
		'form': form,
		}


		return render(request, 'subtribe_edit.html', context)

	else:
		return HttpResponse(status=403)



@login_required
def subtribe_delete(request, id):
	user = request.user
	page_title = "Delete Project"
	instance = get_object_or_404(MySubTribe, id=id)

	if request.user == instance.leader:


		if 'delete' in request.POST:

			print ("Delete")

			instance.delete()
			return redirect ("tribe")

		context = {
		'instance': instance,
		'page_title': page_title,
		}


		return render(request, 'subtribe_delete.html', context)

	else:
		return HttpResponse(status=403)





@login_required
def subtribe_upload_project(request, id):
	page_title = "Upload Project"
	subtribe = get_object_or_404(MySubTribe, id=id)
	profile_name = Profile.objects.get(user=request.user)
	member_check = MySubTribe.objects.filter(id=id, members=profile_name)

	if request.user == subtribe.leader or member_check:

		form = SubTribeProjectForm()

		if request.method == 'POST':

			form = SubTribeProjectForm(request.POST, request.FILES)
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.subtribe = subtribe
				instance.save()

				return redirect("subtribe", id=subtribe.id)


		context = {
		'form': form,
		'page_title': page_title,
		}

		return render(request, 'subtribe_upload_project.html', context)

	else:
		return HttpResponse(status=403)





















@login_required
def get_tribe_audio_project(request, id):
	project = get_object_or_404(TribeAudioProject, id=id)
	page_title = project.title
	comments = TribeComment.objects.filter(project=project).order_by('timestamp')
	form = TribeCommentForm()
	project_friends = Friend.objects.friends(request.user)
	notifications = Notification.objects.filter(user=request.user, tribe_project=id, unread=True).order_by('-timestamp')

	for notification in notifications:
		notification.unread = False
		notification.save()

	if project.user in project_friends or project.user == request.user:

		if request.method == 'POST':

			form = TribeCommentForm(request.POST or None)
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.project = project
				instance.project_user = project.user
				instance.save()

				return redirect("get_tribe_audio_project", id=project.id)

		context = {
			'page_title': page_title,
			'project': project,
			'comments': comments,
			'form': form,
			}

		return render(request, 'tribe_project.html', context)

	else:

		return HttpResponse(status=403)




@login_required
def new_tribe_project(request):
	page_title = "Share With Tribe"

	if request.user.is_authenticated():
		form = TribeProjectForm()

		if request.method == 'POST':
			form = TribeProjectForm(request.POST, request.FILES)
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.save()

				return redirect ("tribe_feed")


		context = {
		'form': form,
		'page_title': page_title,
		}

		return render(request, 'new_tribe_project.html', context)










