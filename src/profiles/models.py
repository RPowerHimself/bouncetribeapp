from __future__ import division
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.timesince import timesince as timesince_


from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from awesome_avatar.fields import AvatarField
from awesome_avatar import forms as avatar_forms
from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer

from django.db.models import signals
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.template import loader

from friendship.models import Friend, Follow, FriendshipRequest

from allauth.utils import get_user_model, get_current_site, serialize_instance, deserialize_instance

from projects.models import Project, ProjectMatch, MatchChatMessage
from tribe.models import TribeAudioProject, TribeComment

from .validators import validate_file_size, validate_file_extension


User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):
	location = str(instance.user.username)
	return "%s/%s" %(location, filename)


def audio_location(instance, filename):
	location = str(instance.user.username)
	return "%s/%s" %(location, filename)


RATINGS = (
		('New Reviewer', 'New Reviewer'),
		('Liked Reviewer', 'Liked Reviewer'), 
		('Helpful Reviewer', 'Helpful Reviewer'),
		('Reviewer Promotion','Reviewer Promotion'),
		('Respected Reviewer','Respected Reviewer'),
		('Revered Reviewer','Revered Reviewer'),
		('Top Reviewer','Top Reviewer'),
		)


SKILLS = (
		('Novice (Just Started)', 'Novice (Just Started)'),
		('Beginner (0-2 Years)', 'Beginner (0-2 Years)'), 
		('Skilled (3-9 Years)', 'Skilled (3-9 Years)'),
		('Accomplished (10-24 Years)','Accomplished (10-24 Years)'),
		('Veteran (25+ Years)','Veteran (25+ Years)'),
		)


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
	name = models.CharField(max_length=120, unique=True)
	location = models.CharField(max_length=30, null=True, blank=True)
	picture = models.ImageField(upload_to=upload_location, null=True, blank=True)
	bio = models.TextField(max_length=150, null=True, blank=True)
	experience = models.CharField(max_length=50, choices=SKILLS, default='Beginner (0-2 Years)')
	email = models.EmailField (max_length=50, null=True, blank=True)
	website = models.CharField(max_length=50, null=True, blank=True)
	influences = models.TextField(max_length=600, null=True, blank=True)
	featured_project = models.ForeignKey('projects.Project', null=True, blank=True, related_name='featured_project')
	current_project = models.ForeignKey('projects.Project', null=True, blank=True, related_name='current_project')
	current_projects = models.IntegerField(default=0)
	total_projects = models.IntegerField(default=0)
	total_likes = models.IntegerField(default=0)
	image = ImageCropField(blank=True, upload_to=upload_location, validators=[validate_file_size])
	cropping = ImageRatioField('image', '200x200')
	rating = models.CharField(max_length=120, choices=RATINGS, default='User Match')

 
	def __unicode__(self):
		return u"%s" % self.user

	def get_absolute_url(self):
		url = reverse("profile", kwargs={"username": self.user.username})
		return url


	def get_absolute_url_notification(self):
		url = reverse("profile", kwargs={"username": self.user.username})
		return url



	def get_thumbnail(self):
		thumbnail_url = get_thumbnailer(self.image).get_thumbnail({
    	'size': (200, 200),
    	'box': self.cropping,
    	'crop': True,
    	'detail': True,
		}).url

		return thumbnail_url


	def reviewer_rating(self):
		rating = "New Reviewer"

		if self.total_likes >= 1000:
			rating = "Top Reviewer"
			self.rating = "Top Reviewer"
			self.save()

		elif self.total_likes >= 100:
			rating = "Revered Reviewer"
			self.rating = "Revered Reviewer"
			self.save()

		elif self.total_likes >= 50:
			rating = "Respected Reviewer"
			self.rating = "Respected Reviewer"
			self.save()

		elif self.total_likes >= 20:
			rating = "Helpful Reviewer"
			self.rating = "Helpful Reviewer"
			self.save()

		elif self.total_likes >= 5:
			rating = "Liked Reviewer"
			self.rating = "Liked Reviewer"
			self.save()

		elif self.total_likes < 5:
			rating = "New Reviewer"

		return rating


	def reviewer_progress(self):

		if self.total_likes >= 1000:
			rating = "Top Reviewer"
			min_likes = self.total_likes - 1000
			max_likes = 4000
			Notification.objects.get_or_create(user=self.user, notification_type="Reviewer Promotion", title="Reviewer Promotion!", text="You are now a Top Reviewer")

		elif self.total_likes >= 100:
			rating = "Revered Reviewer"
			min_likes = self.total_likes - 100
			max_likes = 900
			Notification.objects.get_or_create(user=self.user, notification_type="Reviewer Promotion", title="Reviewer Promotion!", text="You are now a Revered Reviewer")

		elif self.total_likes >= 50:
			rating = "Respected Reviewer"
			min_likes = self.total_likes - 50
			max_likes = 50
			Notification.objects.get_or_create(user=self.user, notification_type="Reviewer Promotion", title="Reviewer Promotion!", text="You are now a Respected Reviewer")

		elif self.total_likes >= 20:
			rating = "Helpful Reviewer"
			min_likes = self.total_likes - 20
			max_likes = 30
			Notification.objects.get_or_create(user=self.user, notification_type="Reviewer Promotion", title="Reviewer Promotion!", text="You are now a Helpful Reviewer")

		elif self.total_likes >= 5:
			rating = "Liked Reviewer"
			min_likes = self.total_likes - 5
			max_likes = 15
			Notification.objects.get_or_create(user=self.user, notification_type="Reviewer Promotion", title="Reviewer Promotion!", text="You are now a Liked Reviewer")

		elif self.total_likes < 5:
			rating = "New Reviewer"
			min_likes = self.total_likes
			max_likes = 5
	
		percentage = (min_likes / max_likes) * 100
		
		return percentage






	def get_total_project(self):
		total_match_projects = Project.objects.filter(user=self.user).count()
		total_tribe_projects = TribeAudioProject.objects.filter(user=self.user).count()
		projects = total_match_projects + total_tribe_projects
		return projects




def profile_callback(sender, request, user, **kwargs):
	profile, is_created = Profile.objects.get_or_create(user=user)
	if is_created:
		profile.name = user.username
		profile.save()


user_logged_in.connect(profile_callback)



class Influence(models.Model):
	user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='influence_user')
	text = models.CharField(max_length=20)

	def __unicode__(self):
		return self.text










class MySubTribe(models.Model):
	leader = models.ForeignKey(User, related_name='my_subtribe_leader')
	name = models.CharField(max_length=20)
	members = models.ManyToManyField('profiles.Profile', related_name='my_subtribe_members')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return "%s - %s" % (self.name, self.leader)


	def get_absolute_url(self):
		url = reverse("subtribe", kwargs={"id": self.id})
		return url


	def total_members(self):
		members = self.members.count() + 1
		return members










class MySubTribeProject(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subtribe_project_user')
	subtribe = models.ForeignKey('profiles.MySubTribe', related_name='my_subtribe')
	title = models.CharField(max_length=30, unique=True, default="Your Project's Title")
	audio_file = models.FileField(upload_to=audio_location, blank=True, validators=[validate_file_extension])
	short_description = models.TextField(max_length=300, blank=True, help_text="Lyrics, notes, or things to keep in mind.")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['-created']


	def __unicode__(self):
		return "%s (%s)" % (self.title, self.subtribe)


	def get_absolute_url(self):
		url = reverse("get_subtribe_audio_project", kwargs={"id": self.id})
		return url


	def subtribe_audio_project_timesince(self, now=None):
		time_now = datetime.now()
		time_elapsed = timesince_(self.created, now).split(', ')[0]
		
		return time_elapsed
















TYPES = (
		('User Match', 'User Match'),
		('Feedback Received', 'Feedback Received'), 
		('Feedback Liked', 'Feedback Liked'),
		('Reviewer Promotion','Reviewer Promotion'),
		('Tribe Request Accepted','Tribe Request Accepted'),
		('Tribe Feedback','Tribe Feedback'),
		('SubTribe Created','SubTribe Created'),

		)





class Notification(models.Model):
	user = models.ForeignKey(User, related_name='notified_user')
	notification_type = models.CharField(max_length=50, choices=TYPES, default='User Match')
	title = models.CharField(max_length=120)
	text = models.CharField(max_length=120)
	from_user = models.ForeignKey(User, related_name='from_user', null=True)
	session = models.ForeignKey('projects.ProjectMatch', null=True, blank=True)
	subtribe = models.ForeignKey('profiles.MySubTribe', null=True, blank=True)
	project = models.ForeignKey('projects.Project', null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)
	unread = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s - %s" % (self.user, self.title)


	def get_session_url(self):
		url = reverse("get_session_notification", kwargs={"id": self.id})
		return url

	def get_chat_url(self):
		url = reverse("get_chat_notification", kwargs={"id": self.id})
		return url

	def get_profile_url(self):
		url = reverse("get_profile_notification", kwargs={"id": self.id})
		return url

	def get_user_profile_url(self):
		url = reverse("get_user_profile_notification", kwargs={"id": self.id})
		return url


	def get_tribe_project_url(self):
		url = reverse("get_tribe_project_notification", kwargs={"id": self.id})
		return url

	def get_subtribe_url(self):
		url = reverse("get_subtribe_notification", kwargs={"id": self.id})
		return url


	def mark_as_read(self):
		self.unread = False
		self.save()
		return redirect('get_all_notifications')


	def timesince(self, now=None):
		from django.utils.timesince import timesince as timesince_

		time_now = datetime.now()
		time_elapsed = timesince_(self.created, now).split(', ')[0]
		
		return time_elapsed
		

	# objects = NotificationManager()


@receiver(post_save, sender=ProjectMatch)
def user_match_notification(sender, instance, created, **kwargs):
	if created:
		Notification.objects.create(user=instance.user_b, from_user=instance.user_a, notification_type="User Match", title="New Match!", text="You have been matched with", session=instance)
		Notification.objects.create(user=instance.user_a, from_user=instance.user_b, notification_type="User Match", title="New Match!", text="You have been matched with", session=instance)

		match_user_b_html_message = loader.render_to_string(
			'notifications/notification-match.html',
			{
				'match_user': instance.user_a,
				'match_id': instance.id,
			}
		)

		match_user_b_message = 'You have been matched with %s' % (instance.user_a)

		send_mail(
    		'New Match!',
    		match_user_b_message,
    		'BounceTribe <notify@bouncetribe.com>',
    		[instance.user_b.email],
    		fail_silently=False,
    		html_message=match_user_b_html_message
		)




@receiver(post_save, sender=Friend)
def friend_request_accepted_notification(sender, instance, created, **kwargs):
	instance = Friend.objects.get(id=instance.id)
	duplicate = Friend.objects.filter(to_user=instance.from_user, from_user=instance.to_user)

	if created:
		if not duplicate:
			Notification.objects.create(user=instance.from_user, from_user=instance.to_user, notification_type="Tribe Request Accepted", title="Tribe Request Accepted!", text="has accepted your request.")



@receiver(post_save, sender=TribeComment)
def tribe_feedback_notification(sender, instance, created, **kwargs):
	if created:
		Notification.objects.create(user=instance.project.user, from_user=instance.user, notification_type="Tribe Feedback", title="Tribe Feedback!", text="has given you some feedback.", project=instance.project)



@receiver(post_save, sender=MatchChatMessage)
def chat_message_notification(sender, instance, created, **kwargs):
	if created:
		Notification.objects.create(user=instance.to_user, from_user=instance.user, notification_type="Chat Message", title="Message Received!", text="sent you a message.", session=instance.session)
		

		chat_message_html_message = loader.render_to_string(
			'notifications/notification-message.html',
			{
				'message': instance.message,
				'from_user': instance.user,
				'chat_id': instance.session.id,
			}
		)

		send_mail(
    		'Message Received!',
    		instance.message,
    		'BounceTribe <notify@bouncetribe.com>',
    		[instance.to_user.email],
    		fail_silently=False,
    		html_message=chat_message_html_message
		)































THUMB_CHOICES = (
	("hd", "HD"),
	("sd", "SD"),
	("micro", "Micro"),
)

class Thumbnail(models.Model):
	user = models.ForeignKey(User, related_name='thumbail_user')
	type = models.CharField(max_length=20, choices=THUMB_CHOICES, default='hd')
	height = models.CharField(max_length=20, null=True, blank=True)
	width = models.CharField(max_length=20, null=True, blank=True)
	media = models.ImageField(
		width_field= "width",
		height_field= "height",
		blank=True,
		null=True,
		upload_to=upload_location
	)

	def __unicode__(self):
		return str(self.media.path)





