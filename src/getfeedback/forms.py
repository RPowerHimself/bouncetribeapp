from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea
from .models import Project


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = [
		"audio_file",
		"title",
		"short_description",
		"genre",
		"experience",
		"match_nearby"
		]
		
		labels = {
		'audio_file': _('Select Your Audio File to Upload'),
		'title': _('Name Your Project'),
		'experience': _('Your Experience Level'),
		'match_nearby': _('Match Nearby'),
		'short_description': _('Briefly Describe Your Project (Optional)'),
		}

		widgets = {
            'short_description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
































# class ProjectForm(forms.Form):
# 	project_id = forms.IntegerField()
# 	answer_id = forms.IntegerField()
# 	importance_level = forms.ChoiceField(choices=LEVELS)
# 	their_answer_id = forms.IntegerField()
# 	their_importance_level = forms.ChoiceField(choices=LEVELS)




	
	# def clean_project_id(self):
	# 	project_id = self.cleaned_data.get('answer_id')
	# 	try:
	# 		obj = Project.objects.get(id=project_id)
	# 	except:
	# 		raise forms.ValidationError('Something went wrong. Please try again.')
	# 	return project_id	


	# def clean_answer_id(self):
	# 	answer_id = self.cleaned_data.get('answer_id')
	# 	try:
	# 		obj = Answer.objects.get(id=answer_id)
	# 	except:
	# 		raise forms.ValidationError('Something went wrong. Please try again.')
	# 	return answer_id



	# def clean_their_answer_id(self):
	# 	their_answer_id = self.cleaned_data.get('their_answer_id')
	# 	try:
	# 		obj = Answer.objects.get(id=their_answer_id)
	# 	except:
	# 		if their_answer_id == -1:
	# 			return their_answer_id
	# 	else:
	# 		raise forms.ValidationError('Something went wrong. Please try again.')
	# 	return their_answer_id

