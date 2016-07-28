from django.conf import settings
from django.db import models


from allauth.account.signals import user_logged_in, user_signed_up





GENRES = (
		('Alternative Rock', 'Alternative Rock'), 
		('Ambient', 'Ambient'),
		('Bluegrass', 'Bluegrass'),
		('Blues','Blues'),
		)


SKILLS = (
		('Beginner', 'Beginner'), 
		('Experienced', 'Experienced'),
		('Seasoned','Seasoned'),
		)


class GetFeedbackProject(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
	title = models.CharField(max_length=120)
	genre = models.CharField(max_length=50, choices=GENRES, default='Alternative Rock')
	skill = models.CharField(max_length=50, choices=SKILLS, default='Beginner')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title