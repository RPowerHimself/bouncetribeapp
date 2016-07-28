import datetime
from django.utils import timezone

from django.conf import settings
from audiofield.fields import AudioField
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.signals import post_save, pre_save
from django.contrib import messages


from .forms import SessionFeedbackForm, MatchFeedbackForm_A, MatchFeedbackForm_B, ChatMessageForm
from .models import SessionFeedback

from projects.models import Project, ProjectMatch, MatchChatMessage
from profiles.models import Profile, Notification

User = get_user_model()



@login_required
def get_session(request, id):
	if request.user.is_authenticated():
		user = request.user 
		instance = get_object_or_404(ProjectMatch, id=id)
		feedback = get_object_or_404(ProjectMatch, id=id)
		notifications = Notification.objects.filter(user=request.user, session=id, unread=True).order_by('-timestamp')

		for notification in notifications:
			notification.unread = False
			notification.save()


		if instance.user_a == user and instance.user_b != user:


			form_b = MatchFeedbackForm_B(instance=feedback)
			page_title = "Feedback - %s" %(instance.user_b)
			context = {
				"instance": instance,
				"form_b": form_b,
				"feedback": feedback,
				"page_title": page_title,
			}


			if request.is_ajax():
				print request.POST

				print ("It Worked!")

				instance_id = request.POST.get("instance_id")
				instance = ProjectMatch.objects.get(id=instance_id)
				user_b = instance.user_b
				instance.user_a_like = True
				instance.save()

				user_b_profile = Profile.objects.get(user=user_b)
				user_b_profile.total_likes += 1
				user_b_profile.save()

				Notification.objects.create(user=user_b, from_user=request.user, notification_type="Feedback Liked", title="Feedback Liked!", text="liked your feedback.", session=instance)

				return JsonResponse(data)


			if 'form_b' in request.POST:

				form_b = MatchFeedbackForm_B(request.POST or None, instance=instance)
				
				if form_b.is_valid():
					instance = form_b.save(commit=False)
					instance.save()

					Notification.objects.create(user=instance.user_b, from_user=instance.user_a, notification_type="Feedback Received", title="Feedback Received!", text="You have received feedback from", session=instance)
				
					return redirect("get_session", id=instance.id)



					
		elif instance.user_b == user and instance.user_a != user:


			form_a = MatchFeedbackForm_A(instance=feedback)
			page_title = "Feedback - %s" %(instance.user_a)
			context = {
				"instance": instance,
				"form_a": form_a, 
				"feedback": feedback,
				"page_title": page_title,
			}


			if request.is_ajax():
				print request.POST
				instance_id = request.POST.get("instance_id")
				instance = ProjectMatch.objects.get(id=instance_id)
				user_a = instance.user_a
				instance.user_b_like = True
				instance.save()

				user_a_profile = Profile.objects.get(user=user_a)
				user_a_profile.total_likes += 1
				user_a_profile.save()

				Notification.objects.create(user=user_a, from_user=request.user, notification_type="Feedback Liked", title="Feedback Liked!", text="liked your feedback.", session=instance)

				return JsonResponse(data)


			if 'form_a' in request.POST:

				form_a = MatchFeedbackForm_A(request.POST or None, instance=instance)
				
				if form_a.is_valid():
					instance = form_a.save(commit=False)
					instance.save()

					Notification.objects.create(user=instance.user_a, from_user=instance.user_b, notification_type="Feedback Received", title="Feedback Received!", text="You have received feedback from", session=instance)

					return redirect("get_session", id=instance.id)


		else:
			raise Http404


		return render(request, "session.html", context)
	else:
		raise Http404("Session does not exist")




@login_required
def session_chat(request, id):
	instance = get_object_or_404(ProjectMatch, id=id)
	chat_message_form = ChatMessageForm()
	messages = MatchChatMessage.objects.filter(session=instance).order_by('timestamp')


	if instance.user_a == request.user:

		to_user = instance.user_b

	else:

		to_user = instance.user_a

	page_title = "Chat - %s" %(to_user)



	if 'chat_message' in request.POST:

		chat_message_form = ChatMessageForm(request.POST)
			
		if chat_message_form.is_valid():
			message_instance = chat_message_form.save(commit=False)
			message_instance.user = request.user
			message_instance.to_user = to_user
			message_instance.session = instance
			message_instance.save()

			return redirect("session_chat", id=instance.id)



	context = { "instance": instance,
				"messages": messages,
				"chat_message_form": chat_message_form,
				"to_user": to_user,
				"page_title": page_title,
			}


	return render(request, "session_chat.html", context)









@login_required
def ajax_test(request, *args, **kwargs):
	user = request.user
	messages = MatchChatMessage.objects.filter(user=request.user).order_by('timestamp')
	projects = Project.objects.filter(user=request.user).order_by('-timestamp')
	
	context = { "messages": messages,
				"user": user,
				"projects": projects

	}
	
	print request.POST.get
	if request.is_ajax():
	
		username = request.POST.get("username")
		data = {
			"works": True,
			"time": datetime.datetime.now(),
		}
		return JsonResponse(data)



	return render(request, "ajax.html", context)









