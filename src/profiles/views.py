from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Count
try:
    from django.contrib.auth import get_user_model
    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
    user_model = Us

from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageCropWidget

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from friendship.exceptions import AlreadyExistsError
from friendship.models import Friend, Follow, FriendshipRequest
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from allauth.utils import get_user_model, get_current_site, serialize_instance, deserialize_instance
from awesome_avatar import forms as avatar_forms

from profiles.forms import ProfileForm, ProfilePhotoForm, ProfileNoPhotoForm
from profiles.models import Profile, Notification, MySubTribe
from projects.models import Project, ProjectMatch
from tribe.models import TribeAudioProject, TribeComment


# User = get_user_model()

get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')
get_friendship_context_object_list_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME', 'users')



@login_required
def home(request):
	page_title = "My Matches"
	if request.user.is_authenticated():
		user = request.user
		matches = []
		match_set = ProjectMatch.objects.matches_all(request.user).order_by('-timestamp')
		# notifications = []
		# notification_set = Notification.objects.filter(user=request.user).order_by('-timestamp')
		# friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True).filter(to_user=request.user)
		projects_queued = Project.objects.filter(user=request.user, queued=True).order_by('-timestamp')
		sessions_total = ProjectMatch.objects.matches_all(request.user).count()

		for match in match_set: 
			if match.user_a == request.user and match.user_b != request.user:
				items_wanted = [match.user_b, match.project_b, match]
				matches.append(items_wanted)
			elif match.user_b == request.user and match.user_a != request.user:
				items_wanted = [match.user_a, match.project_a, match]
				matches.append(items_wanted)
			else:
				pass


		# for notification in notification_set: 
		# 	if notification.user == request.user:
		# 		items_wanted = [notification.title, notification.from_user, notification.text, notification.session, notification]
		# 		notifications.append(items_wanted)
		# 	else:
		# 		pass



		context = {
		'user': user,
		'matches': matches,
		# 'notifications': notifications[:4],
		# 'friendship_requests': friendship_requests[:10],
		'projects_queued': projects_queued[:1],
		'page_title': page_title,
		'sessions_total': sessions_total
		# "time_left": time_left,
		# "timestamp": timestamp,

		}
	return render(request, 'matches.html', context)


@login_required
def get_session_notification(request, id):
	user = request.user
	instance = get_object_or_404(Notification, id=id)

	if request.user == instance.user:

		instance.mark_as_read()

		return redirect("get_session", id=instance.session.id)

	else:
		return HttpResponse(status=403)



@login_required
def get_chat_notification(request, id):
	user = request.user
	instance = get_object_or_404(Notification, id=id)

	if request.user == instance.user:

		instance.mark_as_read()

		return redirect("session_chat", id=instance.session.id)

	else:
		return HttpResponse(status=403)



@login_required
def get_profile_notification(request, id):
	user = request.user
	instance = get_object_or_404(Notification, id=id)

	if request.user == instance.user:

		instance.mark_as_read()

		return redirect("profile", username=instance.from_user.profile.user)

	else:
		return HttpResponse(status=403)



@login_required
def get_user_profile_notification(request, id):
	user = request.user
	instance = get_object_or_404(Notification, id=id)

	if request.user == instance.user:

		instance.mark_as_read()

		return redirect("profile_user")

	else:
		return HttpResponse(status=403)




@login_required
def get_tribe_project_notification(request, id):
	user = request.user
	instance = get_object_or_404(Notification, id=id)

	if request.user == instance.user:

		instance.mark_as_read()

		return redirect("get_project", id=instance.project.id)

	else:
		return HttpResponse(status=403)



@login_required
def get_subtribe_notification(request, id):
	user = request.user
	instance = get_object_or_404(Notification, id=id)

	if request.user == instance.user:

		instance.mark_as_read()

		return redirect("subtribe", id=instance.subtribe.id)

	else:
		return HttpResponse(status=403)




@login_required
def get_all_notifications(request):
	page_title = "Notifications"
	notifications_qs = Notification.objects.filter(user=request.user).order_by('-timestamp')

	paginator = Paginator(notifications_qs, 15)

	page = request.GET.get('page')
	try:
		notifications_list = paginator.page(page)
	
	except PageNotAnInteger:
		notifications_list = paginator.page(1)
	
	except EmptyPage:
		notifications_list = paginator.page(paginator.num_pages)
		


	context = {
	'page_title': page_title,
	'notifications_list': notifications_list,
	}

	return render(request, "notifications_all.html", context)






@login_required
def profile_user(request):
	page_title = "My Profile"
	user = get_object_or_404(User, username=request.user)
	profile, created = Profile.objects.get_or_create(user=user)
	tribe_members = Friend.objects.filter(to_user=user).count

	projects = Project.objects.filter(user=user)
	total_match_projects = Project.objects.filter(user=user).count()
	total_tribe_projects = TribeAudioProject.objects.filter(user=user).count()
	total_projects = total_match_projects + total_tribe_projects
	
	try:
		current_project = Project.objects.filter(user=user, active=True).order_by('-id')[0]

	except:
		current_project = False


	previous_sessions = []
	previous_sessions_set = ProjectMatch.objects.matches_all(request.user).order_by('-timestamp')
	sessions_total = ProjectMatch.objects.matches_all(request.user).count()


	for session in previous_sessions_set: 
			if session.user_a == request.user and session.user_b != request.user:
				items_wanted = [session.user_b, session.project_b, session]
				previous_sessions.append(items_wanted)
			elif session.user_b == request.user and session.user_a != request.user:
				items_wanted = [session.user_a, session.project_a, session]
				previous_sessions.append(items_wanted)
			else:
				pass




	context = {
	'user': user,
	'profile': profile,
	'tribe_members': tribe_members,
	'projects': projects,
	'total_projects': total_projects,
	'sessions_total': sessions_total,
	'page_title': page_title,
	'total_match_projects': total_match_projects,
	'current_project': current_project,

	}
	return render(request, "profile_user.html", context)




@login_required
def profile_view(request, username):
	user = get_object_or_404(User, username=username)
	profile, created = Profile.objects.get_or_create(user=user)
	page_title = profile

	projects = Project.objects.filter(user=user)

	total_match_projects = Project.objects.filter(user=user).count()
	total_tribe_projects = TribeAudioProject.objects.filter(user=user).count()
	total_projects = total_match_projects + total_tribe_projects

	try:
		current_project = Project.objects.filter(user=user, active=True).order_by('-id')[0]

	except:
		current_project = False


	tribe_members = Friend.objects.filter(to_user=user).count
	to_username = user_model.objects.get(username=username)
	from_user= request.user
	to_user= user
	ctx = {'to_username': to_username}
	friends_with = Friend.objects.are_friends(request.user, user)
	

	if Friend.objects.are_friends(request.user, user) == True:
		friends_with = True


	request_sent = FriendshipRequest.objects.filter(from_user=request.user, to_user=user)


	if 'cancel' in request.POST:

			request_sent.delete()
			return redirect("profile", username=username)


	if 'cancel_request' in request.POST:

			request_sent_now = FriendshipRequest.objects.filter(from_user=request.user, to_user=user)
			request_sent_now.delete()
			return redirect("profile", username=username)



	if request.is_ajax():
	    	to_user = user_model.objects.get(username=username)
	    	to_username = user_model.objects.get(username=username)
	    	from_user = request.user
	    	context = {
			'to_username': to_username,
			}
	        try:
	            Friend.objects.add_friend(from_user, to_user)
	        except AlreadyExistsError as e:
	            ctx['errors'] = ["%s" % e]

		return JsonResponse(data)


	if 'remove' in request.POST:

		other_user = user
		Friend.objects.remove_friend(other_user, request.user)
		return redirect("profile", username=username)



	# if request.is_ajax():
	# 	to_user = user_model.objects.get(username=username)
	#     to_username = user_model.objects.get(username=username)
	#     from_user = request.user
	#     context = {
	# 	'to_username': to_username,
	# 	}
	#     try:
	#        	Friend.objects.add_friend(from_user, to_user)
	#     except AlreadyExistsError as e:
	#         ctx['errors'] = ["%s" % e]
	#     else:
	#         return redirect ('profile_view', username=username)

	# # return JsonResponse(data)


	context = {
	'user': user,
	'profile': profile,
	'username': username,
	'tribe_members': tribe_members,
	'friends_with': friends_with,
	'projects': projects,
	'total_projects': total_projects,
	'total_tribe_projects': total_tribe_projects,
	'total_match_projects': total_match_projects,
	'request_sent': request_sent,
	'page_title': page_title,
	'current_project': current_project,
	}
	return render(request, "profile.html", context)



@login_required
def get_previous_sessions(request):
	page_title = "Previous Sessions"
	previous_sessions = []
	previous_sessions_set = ProjectMatch.objects.matches_all(request.user).order_by('-timestamp')
	sessions_total = ProjectMatch.objects.matches_all(request.user).count()

	for session in previous_sessions_set: 
			if session.user_a == request.user and session.user_b != request.user:
				items_wanted = [session.user_b, session.project_b, session.project_a, session]
				previous_sessions.append(items_wanted)
			elif session.user_b == request.user and session.user_a != request.user:
				items_wanted = [session.user_a, session.project_a, session.project_b, session]
				previous_sessions.append(items_wanted)
			else:
				pass


	context = {
	'previous_sessions': previous_sessions,
	'page_title': page_title,
	'sessions_total': sessions_total,
		}

	return render(request, 'previous_sessions.html', context)





@login_required
def profile_edit(request):
	page_title = "Edit Profile"
	profile, created = Profile.objects.get_or_create(user=request.user)
	form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

	projects = Project.objects.filter(user=request.user)
	projects_count = projects.count()
	form.fields["featured_project"].queryset = projects

	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect ("profile_user")

	context = {
	'profile': profile,
	'form': form, 
	'page_title': page_title,
	'projects_count': projects_count,
	}

	return render(request, 'profile_settings.html', context)



@login_required
def profile_photo(request):
	page_title = "Edit Photo"
	profile, created = Profile.objects.get_or_create(user=request.user)
	form = ProfileNoPhotoForm(request.POST or None, request.FILES or None, instance=profile)

	if profile.image and not form.errors:

		form = ProfilePhotoForm(request.POST or None, request.FILES or None, instance=profile)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect ("profile_photo")


	else:

		form = ProfileNoPhotoForm(request.POST or None, request.FILES or None, instance=profile)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect ("profile_photo")


	if form.errors:

		form = ProfileNoPhotoForm(request.POST or None, request.FILES or None, instance=profile)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect ("profile_photo")


	context = {
	'profile': profile,
	'form': form,
	'page_title': page_title,
	}
	return render(request, 'profile_photo.html', context)





@login_required
def friends(request):
	page_title = "My Tribe"
	all_friends = Friend.objects.friends(request.user)
	total_feedbackers = Friend.objects.filter(to_user=request.user).count
	requests = Friend.objects.unread_requests(user=request.user)
	profile_name = Profile.objects.filter(user=request.user)

	# subtribe_leader = MySubTribe.objects.filter(leader=request.user)
	# subtribe_member = MySubTribe.objects.filter(members=profile_name)
	# subtribes = (subtribe_leader | subtribe_member).distinct()
	


	context = {
	'all_friends': all_friends,
	'total_feedbackers': total_feedbackers,
	'page_title': page_title,
	# 'subtribes': subtribes,
	}
	return render(request, 'tribe.html', context)




@login_required
def tribe_find(request):
	page_title = "Add Friends"
	all_friends = Friend.objects.friends(request.user)
	show_results = True


	try:
		qs = Profile.objects.all()
		query = request.GET.get("q")
		qs = qs.filter(
				Q(name__iexact=query)
			).order_by("-name")
	except:
		show_results = False


	context = {
	'show_results': show_results,
	'all_friends': all_friends,
	'page_title': page_title,
	'qs': qs,
	}
	return render(request, 'tribe_find.html', context)

















@login_required
def friendship_accept(request, friendship_request_id):
    """ Accept a friendship request """
    if request.method == 'POST':
        f_request = get_object_or_404(
            request.user.friendship_requests_received,
            id=friendship_request_id)
        f_request.accept()
        return redirect('profile_user')

    return redirect('friendship_requests_detail', friendship_request_id=friendship_request_id)






@login_required
def friendship_request_list(request, template_name='friendship/friend/requests_list.html'):
    """ View unread and read friendship requests """
    # friendship_requests = Friend.objects.requests(request.user)
    friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True)

    return render(request, template_name, {'requests': friendship_requests})














