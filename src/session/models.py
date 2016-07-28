from django.db import models
from django.conf import settings


from projects.models import Project, ProjectMatch
from django.utils import timezone






class SessionFeedback(models.Model):
	user_a_positive_feedback = models.TextField(max_length=500, null=True)
	user_a_negative_feedback = models.TextField(max_length=500, help_text="Please be constructive.", null=True)
	user_b_positive_feedback = models.TextField(max_length=500, null=True)
	user_b_negative_feedback = models.TextField(max_length=500, help_text="Please be constructive.", null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.feedbacker










