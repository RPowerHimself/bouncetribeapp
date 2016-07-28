from django.db import models

from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.timesince import timesince as timesince_


from django.conf import settings
from audiofield.fields import AudioField
from django.db import models
from django.contrib.auth import get_user_model

from django.db.models import signals
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from allauth.account.signals import user_logged_in, user_signed_up
from django.core.urlresolvers import reverse
from allauth.utils import get_user_model, get_current_site, serialize_instance, deserialize_instance

from projects.models import Project
from friendship.models import Friend, Follow, FriendshipRequest
from embed_video.fields import EmbedVideoField

import os.path
from .validators import validate_file_extension, validate_file_size

# User = settings.AUTH_USER_MODEL


TYPES = (
		('Audio Project', 'Audio Project'), 
		('Audio Inspiration','Audio Inspiration'),
		)








class TribeComment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_user')
	project = models.ForeignKey('projects.Project', related_name='comment_project')
	project_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_project_user', blank=True, null=True)
	positive_feedback = models.TextField(max_length=600, blank=True, null=True)
	negative_feedback = models.TextField(max_length=600, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return "%s - %s" % (self.project, self.user)

	def comment_timesince(self, now=None):
		time_now = datetime.now()
		time_elapsed = timesince_(self.created, now).split(', ')[0]
		
		return time_elapsed



def upload_location(instance, filename):
	location = str(instance.user.username)
	return "%s/%s" %(location, filename)


class TribeAudioInspiration(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='inspiration_user')
	title = models.CharField(max_length=50)
	artist = models.CharField(max_length=50)
	video = EmbedVideoField(null=True, blank=True)
	artwork = models.ImageField(upload_to=upload_location, null=True, blank=True, validators=[validate_file_size])
	comments = models.TextField(max_length=300, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)
	item_type = models.CharField(max_length=50, choices=TYPES, default='Audio Inspiration')

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return "%s - %s" % (self.title, self.user)


	def audio_inspiration_timesince(self, now=None):
		time_now = datetime.now()
		time_elapsed = timesince_(self.created, now).split(', ')[0]
		
		return time_elapsed





class TribeFeedItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feed_item_user')
	project = models.ForeignKey('projects.Project', null=True, blank=True, related_name='feed_item_project')
	inspiration = models.ForeignKey('tribe.TribeAudioInspiration', null=True, blank=True, related_name='feed_item_inspiration')
	item_type = models.CharField(max_length=50, choices=TYPES, default='Audio Inspiration')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return "%s - %s" % (self.item_type, self.user)




@receiver(post_save, sender=TribeAudioInspiration)
def audio_inspiration_item(sender, instance, created, **kwargs):
	if created:
		TribeFeedItem.objects.create(user=instance.user, inspiration=instance, item_type='Audio Inspiration')


@receiver(post_save, sender=Project)
def audio_project_item(sender, instance, created, **kwargs):
	if created:
		TribeFeedItem.objects.create(user=instance.user, project=instance, item_type='Audio Project')











def audio_location(instance, filename):
	location = str(instance.user.username)
	return "%s/%s" %(location, filename)





GENRES = (
		('Alternative Rock', 'Alternative Rock'), 
		('Ambient', 'Ambient'),
		('Christian Rock','Christian Rock'),
		('Christian Gospel', 'Christian Gospel'),
		('Classical', 'Classical'),
		('Comedy','Comedy'),
		('Country', 'Country'),
		('Dance & EDM', 'Dance & EDM'),
		('Deep House', 'Deep House'),
		('Disco', 'Disco'),
		('Dubstep','Dubstep'),
		('Electronic','Electronic'),
		('Folk','Folk'),
		('Funk','Funk'),
		('Hip Hop & Rap','Hip Hop & Rap'),
		('House','House'),
		('Indie','Indie'),
		('Instrumental','Instrumental'),
		('Jazz','Jazz'),
		('Metal','Metal'),
		('Pop','Pop'),
		('Pop Rock','Pop Rock'),
		('R&B Soul','R&B Soul'),
		('Reggae','Reggae'),
		('Rock','Rock'),
		('Ska','Ska'),
		('Singer-Songwriter','Singer-Songwriter'),
		('Soundtrack','Soundtrack'),
		('Techno','Techno'),
		('Trance','Trance'),
		('Trap','Trap'),
		('Trip Hop','Trip Hop'),
		('World','World'),
		('Other','Other'),
		)



class TribeAudioProject(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tribe_project_user')
	title = models.CharField(max_length=30, unique=True, default="Your Project's Title")
	genre = models.CharField(max_length=50, choices=GENRES, default='Alternative Rock')
	audio_file = models.FileField(upload_to=audio_location, blank=True, validators=[validate_file_extension])
	short_description = models.TextField(max_length=300, blank=True, help_text="Lyrics, notes, or things to keep in mind.")
	incomplete = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)
	active = models.BooleanField(default=True)
	item_type = models.CharField(max_length=50, choices=TYPES, default='Audio Project')

	class Meta:
		ordering = ['-created']


	def __unicode__(self):
		return self.title


	def get_absolute_url(self):
		url = reverse("get_tribe_audio_project", kwargs={"id": self.id})
		return url


	def audio_project_timesince(self, now=None):
		time_now = datetime.now()
		time_elapsed = timesince_(self.created, now).split(', ')[0]
		
		return time_elapsed






class SubTribe(models.Model):
	leader = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subtribe_leader')
	name = models.CharField(max_length=20)
	members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subtribe_members')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return "%s - %s" % (self.name, self.leader)


	def get_absolute_url(self):
		url = reverse("subtribe", kwargs={"id": self.id})
		return url


