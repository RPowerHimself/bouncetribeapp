from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from profiles.models import Profile, Notification
from friendship.models import Friend, Follow, FriendshipRequest
from django.contrib.auth.decorators import login_required
from django.utils.functional import SimpleLazyObject




def nav_notifications(request):
	

	def notifications_query():

		notifications = []
		notification_set = Notification.objects.filter(user=request.user).order_by('-timestamp')
		

		for notification in notification_set: 
			if notification.user == request.user:
				items_wanted = [notification.title, notification.from_user, notification.text, notification.session, notification]
				notifications.append(items_wanted)
			else:
				pass

		return notifications[:4]


	def notifications_count():

		total_notifications = Notification.objects.filter(user=request.user, unread=True).count()
		total_friends_requests = FriendshipRequest.objects.filter(rejected__isnull=True).filter(to_user=request.user).count()
		total = total_notifications + total_friends_requests

		return total




	def friends_query():

		friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True).filter(to_user=request.user)

		return friendship_requests[:10]


	return {
        'notifications': SimpleLazyObject(notifications_query),
        'friendship_requests': SimpleLazyObject(friends_query),
        'total_notifications': SimpleLazyObject(notifications_count),
        }





