from django.conf import settings
from audiofield.fields import AudioField
from django.db import models
import datetime
from decimal import Decimal

from django.utils import timezone
from datetime import timedelta
from django.utils.timesince import timesince as timesince_



from django.db.models import signals
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from allauth.account.signals import user_logged_in, user_signed_up
from django.utils import timezone

from django.core.urlresolvers import reverse


from django.core.mail import send_mail

import os.path
from .validators import validate_file_extension



# User = settings.AUTH_USER_MODEL



# class audio_file(models.Model):
# 	name = models.CharField(max_length=120)
# 	audio_file = models.ImageField(upload_to=upload_location, null=True, blank=True)
# 	user = models.ForeignKey(User)
# 	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

# 	def __unicode__(self):
# 		return self.name



# Add this method to your model
def audio_file_player(self):
    """audio player tag for admin"""
    if self.audio_file:
        file_url = settings.MEDIA_URL + str(self.audio_file)
        player_string = '<ul class="playlist"><li style="width:250px;">\
        <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
        return player_string

audio_file_player.allow_tags = True
audio_file_player.short_description = ('Audio file player')




def audio_location(instance, filename):
	location = str(instance.user.username)
	return "%s/%s" %(location, filename)



GENRES = (
		('Christian & Gospel', 'Christian & Gospel'),
		('Classical', 'Classical'),
		('Country', 'Country'),
		('EDM & Electronic', 'EDM & Electronic'),
		('Folk','Folk'),
		('Hip Hop & Rap','Hip Hop & Rap'),
		('Instrumental','Instrumental'),
		('Jazz','Jazz'),
		('Metal','Metal'),
		('Pop','Pop'),
		('Pop Rock','Pop Rock'),
		('R&B Soul','R&B Soul'),
		('Hard Rock','Hard Rock'),
		('Singer-Songwriter','Singer-Songwriter'),
		('Other','Other (Please Describe)'),
		)




SKILLS = (
		('Novice (Just Started)', 'Novice (Just Started)'),
		('Beginner (0-2 Years)', 'Beginner (0-2 Years)'), 
		('Skilled (3-5 Years)', 'Skilled (3-5 Years)'),
		('Seasoned (6+ Years)','Seasoned (6+ Years)'),
		)



class Project(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_user')
	title = models.CharField(max_length=40, unique=True, default='My Project')
	genre = models.CharField(max_length=50, choices=GENRES, default='EDM & Electronic')
	# experience = models.CharField(max_length=50, choices=SKILLS, default='Novice')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	queued = models.BooleanField(default=True)
	audio_file = models.FileField(upload_to=audio_location, blank=True, validators=[validate_file_extension])
	match_nearby = models.BooleanField(default=False)
	short_description = models.TextField(max_length=300, blank=True, help_text="Lyrics, notes, or things to keep in mind.")
	latitude = models.CharField(max_length=100, blank=True, null=True)
	longitude = models.CharField(max_length=100, blank=True, null=True)
	matched_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='matched_users', blank=True)
	created = models.DateTimeField(default=timezone.now)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title


	def get_absolute_url(self):
		url = reverse("get_project", kwargs={"id": self.id})
		return url

	def project_timesince(self, now=None):
		from datetime import datetime, timedelta
		time_now = datetime.now()
		time_elapsed = timesince_(self.created, now).split(', ')[0]
		
		return time_elapsed

	def get_matches_count(self):
		count = self.matched_users.count()
		return count


class ProjectMatchQuerySet(models.query.QuerySet):
	def all(self):
		# return self

		return self.filter(active=True)

	def matches(self, user):
		q1 = self.filter(user_a = user).exclude(user_b=user)
		q2 = self.filter(user_b = user).exclude(user_a=user)
		return (q1 | q2).distinct()


class ProjectMatchManager(models.Manager):
	def get_queryset(self):
		return ProjectMatchQuerySet(self.model, using=self._db)


	def matches_all(self, user):
		return self.get_queryset().matches(user).all()



class ProjectMatch(models.Model):
	user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
	user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
	project_a = models.ForeignKey('projects.Project', related_name='project_a_id')
	project_b = models.ForeignKey('projects.Project', related_name='project_b_id')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	active = models.BooleanField(default=True)
	user_a_positive_feedback = models.TextField(max_length=1000, blank=True, null=True)
	user_a_negative_feedback = models.TextField(max_length=1000, blank=True, null=True, help_text="Please be constructive.")
	user_a_like = models.BooleanField(default=False)
	user_b_positive_feedback = models.TextField(max_length=1000, blank=True, null=True)
	user_b_negative_feedback = models.TextField(max_length=1000, blank=True, null=True, help_text="Please be constructive.")
	user_b_like = models.BooleanField(default=False)

	def __unicode__(self):
		# return u"%s" % self.id
		return "%s - %s - %s" % (self.id, self.user_a, self.user_b)


	def get_absolute_url(self):
		url = reverse("get_session", kwargs={"id": self.id})
		return url


	def get_absolute_url_notification(self):
		url = reverse("get_session", kwargs={"id": self.id})
		return url


	def feedback_for_user_a(self):
		if self.user_a_positive_feedback and self.user_a_negative_feedback:
			return True


	def feedback_for_user_b(self):
		if self.user_b_positive_feedback and self.user_b_negative_feedback:
			return True




	def get_session_timer(self):
		now = timezone.now()
		timestamp = self.timestamp
		time_left = "1 week left"
		offset_7 = now - datetime.timedelta(hours=24)
		offset_6 = now - datetime.timedelta(hours=48)
		offset_5 = now - datetime.timedelta(hours=72)
		offset_4 = now - datetime.timedelta(hours=96)
		offset_3 = now - datetime.timedelta(hours=120)
		offset_2 = now - datetime.timedelta(hours=144)
		offset_1 = now - datetime.timedelta(hours=168)

		if timestamp >= offset_7:
			time_left = "7 days left"
			return time_left

		elif timestamp >= offset_6:
			time_left = "6 days left"
			return time_left

		elif timestamp >= offset_5:
			time_left = "5 days left"
			return time_left

		elif timestamp >= offset_4:
			time_left = "4 days left"
			return time_left	

		elif timestamp >= offset_3:
			time_left = "3 days left"
			return time_left

		elif timestamp >= offset_2:
			time_left = "2 days left"
			return time_left

		elif timestamp >= offset_1:
			time_left = "1 day left"
			return time_left

		elif timestamp <= offset_1:
			time_left = "Expired"
			self.active = False
			self.save()
			return time_left 

		else:
			return time_left


	objects = ProjectMatchManager()




class MatchChatMessage(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='message_user')
	message = models.TextField(max_length=600, blank=True, null=True)
	session = models.ForeignKey('projects.ProjectMatch')
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='message_to_user', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return "%s - %s" % (self.session, self.user)


	def get_absolute_url(self):
		url = reverse("session_chat", kwargs={"id": self.id})
		return url

	def message_timesince(self, now=None):
		time_now = datetime.now()
		time_elapsed = timesince_(self.created, now).split(', ')[0]
		
		return time_elapsed


















class TribeProject(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=30, unique=True, default="Your Project's Title")
	genre = models.CharField(max_length=50, choices=GENRES, default='Alternative Rock')
	audio_file = models.FileField(upload_to=audio_location, blank=True, validators=[validate_file_extension])
	short_description = models.TextField(max_length=300, blank=True, help_text="Lyrics, notes, or things to keep in mind.")
	# matched_users = models.ManyToManyField(User, related_name='matched_users', blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	created = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.title
	




		