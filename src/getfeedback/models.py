from django.conf import settings
from audiofield.fields import AudioField
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from allauth.account.signals import user_logged_in, user_signed_up



import os.path
from .validators import validate_file_extension

# Create your models here.

User = settings.AUTH_USER_MODEL



# class audio_file(models.Model):
# 	name = models.CharField(max_length=120)
# 	audio_file = models.ImageField(upload_to=upload_location, null=True, blank=True)
# 	user = models.ForeignKey(User)
# 	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

# 	def __unicode__(self):
# 		return self.name



# Add the audio field to your model


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




SKILLS = (
		('Novice', 'Novice (Just Started)'),
		('Beginner', 'Beginner (0-2 Years)'), 
		('Skilled', 'Skilled (3-5 Years)'),
		('Seasoned','Seasoned (6+ Years)'),
		)



class Project(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=120, default="Your Project's Title")
	genre = models.CharField(max_length=50, choices=GENRES, default='Alternative Rock')
	experience = models.CharField(max_length=50, choices=SKILLS, default='Novice')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	queued = models.BooleanField(default=True)
	audio_file = models.FileField(upload_to=audio_location, blank=True, validators=[validate_file_extension])
	match_nearby = models.BooleanField(default=True)
	short_description = models.TextField(max_length=300, blank=True, help_text="Anything we should know?")
	# audio_file = AudioField(upload_to=audio_location, blank=True,
 #                        ext_whitelist=(".mp3", ".wav", ".ogg"),
 #                        help_text=("Allowed type - .mp3, .wav, .ogg"))

	def __unicode__(self):
		return self.title



class ProjectMatch(models.Model):
	name = models.CharField(max_length=120, null=True, default="Name")
	user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_a')
	user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='match_user_b')
	project_a = models.ForeignKey(Project, related_name='project_a_id')
	project_b = models.ForeignKey(Project, related_name='project_b_id')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.name



class Match(models.Model):
	name = models.CharField(max_length=120, null=True, default="Name")
	user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_a')
	user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_b')
	project_a_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_a')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.id






# # def match_project(sender, instance, created, *args, **kwargs):
# # 	if created:

# 		if request.user.is_authenticated():

# 		match = Project.objects.filter(queued=True)
# 			for project in match: print (project.id)

			
# 			match_user_a = request.user
# 			match_user_b = project.user

# 			project_a = Project() # Creates instance
# 			project_a.user = request.user
# 			project_a.id = project.id

# 			project_instance = Project.objects.get(id=project.id)
# 			project_a.save() # Saves instance


# 			match_id = project.id

# 		project_id = Project.objects.get(id=17)
# 		project_id = project.id


# 		instance_id = form.cleaned_data.get('project_id') # Gets from form fields
# 		project_a_id = Project.objects.get(id=instance_id) # Gets from model

			
# 		project.queued = False
# 		project.save()

# 		Match.objects.create(
# 			user_a = match_user_a
# 			user_b = match_user_b
# 			project_a_id = 
# 			project_b_id = match_id 
# 			)

# post_save.connect(match_project, sender=Project)


# # match = Match.objects.create(user_a = match_user, user_b = match_user, project_a_id = project.id)

# queryset = Project.objects.all().order_by('-timestamp')
# instance = get_object_or_404(Project, id=id)





































# class Answer(models.Model):
# 	project = models.ForeignKey(Project)
# 	text = models.CharField(max_length=120)
# 	active = models.BooleanField(default=True)
# 	draft = models.BooleanField(default=False)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


# 	def __unicode__(self):
# 		return self.text[:10]


# LEVELS = (
# 		('Mandatory', 'Mandatory'), 
# 		('Very Important', 'Very Important'),
# 		('Somewhat Important', 'Somewhat Important'),
# 		('Not Important','Not Important'),
# 		)


# class UserAnswer(models.Model):
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL)
# 	project = models.ForeignKey(Project)
# 	my_answer = models.ForeignKey(Answer, related_name='user_answer')
# 	my_answer_importance = models.CharField(max_length=50, choices=LEVELS)
# 	my_points = models.IntegerField(default=-1)
# 	their_answer = models.ForeignKey(Answer, null=True, blank=True, related_name='match_answer')
# 	their_importance = models.CharField(max_length=50, choices=LEVELS)
# 	their_points = models.IntegerField(default=-1)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)



# 	def __unicode__(self):
# 		return self.my_answer.text[:10]



# def score_importance(importance_level):
# 	if importance_level == "Mandatory":
# 		points = 300
# 	elif importance_level == "Very Important":
# 		points = 200
# 	elif importance_level == "Somewhat Important":
# 		points = 50
# 	elif importance_level == "Not Important":
# 		points = 0
# 	else:
# 		points = 0
# 	return points



# @receiver(pre_save, sender=UserAnswer)
# def update_user_answer_score(sender, instance, *args, **kwargs): 
# 	my_points = score_importance(instance.my_answer_importance)
# 	instance.my_points = my_points
# 	their_points = score_importance(instance.their_importance)
# 	instance.their_points = their_points









