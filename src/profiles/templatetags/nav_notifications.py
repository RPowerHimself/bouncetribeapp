from django import template
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from profiles.models import Profile, Notification

register = template.Library()


@register.inclusion_tag('navbar.html')
def nav_notifications(request, *args, **kwargs):
	if request.user.is_authenticated():
		notifications = []
		notification_set = Notification.objects.filter(user=request.user).order_by('-timestamp')
		# friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True).filter(to_user=request.user)

		for notification in notification_set: 
			if notification.user == request.user:
				items_wanted = [notification.title, notification.from_user, notification.text, notification.session, notification]
				notifications.append(items_wanted)
			else:
				pass

		return {
		"notifications": notifications,
		}










# @register.simple_tag(takes_context=True)
# def nav_notifications(context, request, *args, **kwargs):
# 	user = request.user
# 	if request.user.is_authenticated():
# 		notifications = []
# 		notification_set = Notification.objects.filter(user=request.user).order_by('-timestamp')
# 		# friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True).filter(to_user=request.user)

# 		for notification in notification_set: 
# 			if notification.user == request.user:
# 				items_wanted = [notification.title, notification.from_user, notification.text, notification.session, notification]
# 				notifications.append(items_wanted)
# 			else:
# 				pass

# 		notifications = context['notifications']

# 		# context = {
# 		# 		"notifications": notifications,
# 		# 	}

# 		return nav_notifications(notifications)




