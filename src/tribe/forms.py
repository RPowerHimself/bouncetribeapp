from django.conf import settings
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea

from tribe.models import TribeAudioProject, TribeComment, TribeAudioInspiration, SubTribe
from profiles.models import MySubTribe, MySubTribeProject





class TribeCommentForm(forms.ModelForm):

	class Meta:
		model = TribeComment

		fields = [
		"positive_feedback",
		"negative_feedback",
		]

		labels = {
		"positive_feedback": _('What do you like?'),
		"negative_feedback": _('What would you suggest changing?'),
		}

		widgets = {
            'positive_feedback': Textarea(attrs={'cols': 60, 'rows': 2}),
            'negative_feedback': Textarea(attrs={'cols': 60, 'rows': 2}),
        }







class SubTribeForm(forms.ModelForm):

	class Meta:
		model = MySubTribe

		fields = [
		"name",
		"members",
		]
		
		labels = {
		'name': _('Name Your SubTribe'),
		'members': _('Members'),
		}

		widgets = {
            'members': forms.CheckboxSelectMultiple()
        }


class SubTribeEditForm(forms.ModelForm):

	class Meta:
		model = MySubTribe

		fields = [
		"members",
		]
		
		labels = {
		'members': _('Members'),
		}

		widgets = {
            'members': forms.CheckboxSelectMultiple()
        }




class SubTribeProjectForm(forms.ModelForm):

	class Meta:
		model = MySubTribeProject

		fields = [
		"audio_file",
		"title",
		"short_description",
		]
		
		labels = {
		'audio_file': _('Select Your Audio File to Upload (.MP3 or .WAV'),
		'title': _('Name Your Project'),
		'short_description': _('Briefly Describe Your Project (Optional)'),
		}

		widgets = {
            'short_description': Textarea(attrs={'cols': 80, 'rows': 5}),

                }





























class TribeProjectForm(forms.ModelForm):

	class Meta:
		model = TribeAudioProject

		fields = [
		"audio_file",
		"title",
		"short_description",
		"genre",
		"incomplete"
		]
		
		labels = {
		'audio_file': _('Select Your Audio File to Upload (.MP3 or .WAV'),
		'title': _('Name Your Project'),
		'short_description': _('Briefly Describe Your Project (Optional)'),
		'incomplete': _('Work In Progress'),
		}

		widgets = {
            'short_description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }








class TribeAudioInspirationForm(forms.ModelForm):

	class Meta:
		model = TribeAudioInspiration

		fields = [
		"title",
		"artist",
		"video",
		"comments",
		]
		
		labels = {
		'title': _('Title'),
		'artist,': _('Artist'),
		}

		widgets = {
            'comments': Textarea(attrs={'cols': 80, 'rows': 3}),
            'title': forms.TextInput(attrs={'placeholder': 'Track Title'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Performer or Group'}),
            'video': forms.TextInput(attrs={'placeholder': 'http://'}),
        }














