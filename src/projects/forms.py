from django.conf import settings
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea, RadioSelect
from .models import Project, ProjectMatch

from formatChecker import RestrictedFileField




User = settings.AUTH_USER_MODEL


class ProjectForm(forms.ModelForm):


	class Meta:
		model = Project
		fields = [
		"audio_file",
		"title",
		"short_description",
		"genre",
		"queued",
		"match_nearby",
		]
		
		labels = {
		'audio_file': _('Select Your Audio File to Upload (.MP3 or .WAV'),
		'title': _('Title'),
		'queued': _('Get Matched'),
		'match_nearby': _('Match Nearby'),
		'short_description': _('Briefly Describe Your Project (Optional)'),
		}

		widgets = {
            'short_description': Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': "I'm wondering if..."}),
            # 'title': forms.TextInput(attrs={'placeholder': 'Name Your Project'}),
            # 'queued': RadioSelect(choices=[
            # (True, 'Yes'),
        #     # (False, 'Share with Tribe Only')             
        # ])
        }




class ProjectEditForm(forms.ModelForm):


	class Meta:
		model = Project
		fields = [
		"title",
		"short_description",
		"match_nearby",
		"genre",
		]
		
		labels = {
		'title': _('Title'),
		'match_nearby': _('Match Nearby'),
		'short_description': _('Briefly Describe Your Project (Optional)'),
		}

		widgets = {
            'short_description': Textarea(attrs={'cols': 80, 'rows': 5}),

        }











class UploadProjectForm1(forms.ModelForm):

	class Meta:
		model = Project
		fields = [
		"audio_file",
		]
		
		labels = {
		'audio_file': _('Select Your Audio File to Upload (.MP3 or .WAV'),
		}


class UploadProjectForm2(forms.ModelForm):


	class Meta:
		model = Project
		fields = [
		"title",
		"short_description",
		"genre",
		"match_nearby"
		]
		
		labels = {
		'title': _('Name Your Project'),
		'match_nearby': _('Match Nearby'),
		'short_description': _('Briefly Describe Your Project (Optional)'),
		}

		widgets = {
            'short_description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }





