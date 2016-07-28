from django.conf import settings
from audiofield.fields import AudioField
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProjectForm
from .models import Project, ProjectMatch


User = get_user_model()


def getfeedback(request):
	if request.user.is_authenticated():
		form = ProjectForm()
		if request.method == 'POST':
			form = ProjectForm(request.POST, request.FILES)
			
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				# instance.save()
				# return redirect ("home")

				instance_genre = form.cleaned_data.get('genre')

				match = Project.objects.filter(queued=True)
				for project in match: print (project.id)

				user_a = request.user
				user_b = project.user
				project_a = Project.objects.get(id=instance.id)
				project_b = Project.objects.get(id=project.id)

				if project.genre == instance_genre:
					ProjectMatch.objects.create(user_a=user_a, user_b=user_b, project_a=project_a, project_b=project_b)
					instance.save()
					return redirect ("home")

				else:
					instance.save()
					return redirect ("home")

		context = {
		'form': form, 
		}

		return render(request, 'getfeedback.html', context)
















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
	
