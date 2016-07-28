from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up

from profiles.models import Profile
from projects.models import Project

# Create your models here.


# class Match(models.Model):
# 	user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
# 	user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
# 	project_a_id = models.OneToOneField()
# 	project_b_id = models.OneToOneField()
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

# 	def __unicode__(self):
# 		return self.id

# 	objects = MatchManager()
	








# class MatchManager(models.Manager):
# 	def get_or_create_match(self, user_a=None, user_b=None):
# 		try:
# 			obj = self.get(user_a=user_a, user_b=user_b)
# 		except:
# 			obj = None
# 		try:
# 			obj_2 = self.get(user_a=user_b, user_b=user_a)
# 		except:
# 			obj_2 = None

# 		if obj and not obj_2:
# 			return obj, False
# 		elif not obj and obj_2:
# 			return obj_2, False
# 		else:
# 			new_instance = self.create(user_a=user_a, user_b=user_b)
# 			new_instance.save()
# 			return new_instance, True



# def get_projects(user_a, user_b):
# 	user_a_project = 
# 	user_b_project = 

