
# # Models.py


# from django.conf import settings
# from django.db import models
# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver

# from profiles.models import Profile


# class Project(models.Model):
# 	text = models.TextField()
# 	## project_file = models.ImageField(upload_to=upload_location, null=True, blank=True)
# 	active = models.BooleanField(default=True)
# 	draft = models.BooleanField(default=False)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	## answers = models.ManyToManyField('Answer')

# 	def __unicode__(self):
# 		return self.text[:10]


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








# # Forms.py



# from django import forms

# from .models import LEVELS, Answer, Project


# class ProjectForm(forms.Form):
# 	project_id = forms.IntegerField()
# 	answer_id = forms.IntegerField()
# 	importance_level = forms.ChoiceField(choices=LEVELS)
# 	their_answer_id = forms.IntegerField()
# 	their_importance_level = forms.ChoiceField(choices=LEVELS)

	
# 	def clean_project_id(self):
# 		project_id = self.cleaned_data.get('answer_id')
# 		try:
# 			obj = Project.objects.get(id=project_id)
# 		except:
# 			raise forms.ValidationError('Something went wrong. Please try again.')
# 		return project_id	


# 	def clean_answer_id(self):
# 		answer_id = self.cleaned_data.get('answer_id')
# 		try:
# 			obj = Answer.objects.get(id=answer_id)
# 		except:
# 			raise forms.ValidationError('Something went wrong. Please try again.')
# 		return answer_id



# 	def clean_their_answer_id(self):
# 		their_answer_id = self.cleaned_data.get('their_answer_id')
# 		try:
# 			obj = Answer.objects.get(id=their_answer_id)
# 		except:
# 			if their_answer_id == -1:
# 				return their_answer_id
# 		else:
# 			raise forms.ValidationError('Something went wrong. Please try again.')
# 		return their_answer_id










# # View.py



# from django.http import Http404
# from django.shortcuts import render, get_object_or_404, redirect


# from .forms import ProjectForm
# from .models import Project, Answer, UserAnswer


# def single(request, id):
	
# 	if request.user.is_authenticated():

# 		queryset = Project.objects.all().order_by('-timestamp')
# 		instance = get_object_or_404(Project, id=id)

# 		try:
# 			user_answer = UserAnswer.objects.get(user=request.user, project=instance)
# 		except UserAnswer.DoesNotExist:
# 			user_answer = UserAnswer()
# 		except UserAnswer.MultipleObjectsReturned:
# 			user_answer = UserAnswer.objects.filter(user=request.user, project=instance)[0]
# 		except:
# 			user_answer = UserAnswer()


# 		form = ProjectForm(request.POST or None)
# 		if form.is_valid():
# 			print form.cleaned_data
# 			# print request.POST
			
# 			project_id = form.cleaned_data.get('project_id')
			
# 			answer_id = form.cleaned_data.get('answer_id')
# 			importance_level = form.cleaned_data.get('importance_level')

# 			their_importance_level = form.cleaned_data.get('their_importance_level')
# 			their_answer_id = form.cleaned_data.get('their_answer_id')


# 			project_instance = Project.objects.get(id=project_id)
# 			answer_instance = Answer.objects.get(id=answer_id)
			
	
# 			user_answer.user = request.user
# 			user_answer.project = project_instance
# 			user_answer.my_answer = answer_instance
# 			user_answer.my_answer_importance = importance_level
# 			if their_answer_id != -1:
# 				their_answer_instance = Answer.objects.get(id=their_answer_id)
# 				user_answer.their_answer = their_answer_instance
# 				user_answer.their_importance = their_importance_level		
# 			else:
# 				user_answer.their_answer = None
# 				user_answer.their_importance = "Not Important"
# 			user_answer.save()



# 			next_p = Project.objects.all().order_by("?").first()
# 			return redirect("getfeedback_single", id=next_p.id)


# 		context = {
# 			"form": form,
# 			"instance": instance,
# 			"user_answer": user_answer,
# 		}
# 		return render(request, "getfeedback/single.html", context)
# 	else:
# 		raise Http404




# def upload_project(request):
# 	if request.user.is_authenticated():
# 		form = ProjectForm(request.POST or None)
# 		if form.is_valid():
# 			project_id = form.cleaned_data.get('project_id')
# 			answer_id = form.cleaned_data.get('answer_id')
# 			project_instance = Project.objects.get(id=project_id)
# 			answer_instance = Answer.objects.get(id=answer_id)
# 			print answer_instance.text, project_instance.text


# 		queryset = Project.objects.all().order_by('-timestamp')
# 		instance = queryset[1]
# 		context = {
# 			"form": form,
# 			"instance": instance,
# 		}
# 		return render(request, "getfeedback.html", context)
# 	else:
# 		raise Http404







# # admin.py


# from django.contrib import admin

# # Register your models here.

# from .models import Project, Answer, UserAnswer


# class AnswerTabularInline(admin.TabularInline):
# 	model = Answer


# class ProjectAdmin(admin.ModelAdmin):
# 	inlines = [AnswerTabularInline]
# 	class Meta:
# 		model = Project


# admin.site.register(Project, ProjectAdmin)

# admin.site.register(Answer)

# admin.site.register(UserAnswer)
















# # Single Template


# {% extends 'base.html' %}
# {% load staticfiles %}


# {% block content %}

# <h1>Get Feedback</h1>


# <form method='POST' action'' > {% csrf_token %}
# {{ form.errors }}
# <h2>{{ instance.text }}</h2>

# <input type='hidden' name='project_id' value='{{ instance.id }}' />

# <h3>Your Answer</h3>
# {% for ans in instance.answer_set.all %}
# <input type='radio' name='answer_id' value='{{ ans.id }}' {% if user_answer.my_answer.id == ans.id %}checked=checked{% endif %} /> {{ ans.text }} <br/>
# {% endfor %}

# <br/>
# Importance: {{ form.importance_level }}

# <h3>Their Ideal Answer</h3>
# {% for ans in instance.answer_set.all %}
# <input type='radio' name='their_answer_id' value='{{ ans.id }}' {% if user_answer.their_answer.id == ans.id %}checked=checked{% endif %} /> {{ ans.text }} <br/>
# {% endfor %}
# <input type='radio' name='their_answer_id' value='-1' {% if not user_answer.their_answer %} checked=checked {% endif %} /> Holds no importance <br/>


# <br/>
# Importance: {{ form.their_importance_level }} <br/><br/>





# <input type='submit' value='Save and continue' />


# </form>



# {% endblock %}

	














