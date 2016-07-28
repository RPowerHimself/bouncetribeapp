from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

import random

from .models import SessionFeedback
from projects.models import Project, ProjectMatch, MatchChatMessage





class SessionFeedbackForm(forms.ModelForm):
	class Meta:
		model = SessionFeedback
		fields = [
		"user_a_positive_feedback",
		"user_a_negative_feedback",
		"user_b_positive_feedback",
		"user_b_negative_feedback",
		]

		labels = {
		"user_a_positive_feedback": _('What do you like?'),
		"user_a_negative_feedback": _('What would you change?'),
		"user_b_positive_feedback": _('What do you like?'),
		"user_b_negative_feedback": _('What would you change?'),

		}

		widgets = {
            'user_a_positive_feedback': Textarea(attrs={'cols': 80, 'rows': 5}),
            'user_a_negative_feedback': Textarea(attrs={'cols': 80, 'rows': 5}),
            'user_b_positive_feedback': Textarea(attrs={'cols': 80, 'rows': 5}),
            'user_b_negative_feedback': Textarea(attrs={'cols': 80, 'rows': 5}),
        }




class MatchFeedbackForm_A(forms.ModelForm):
	class Meta:

		positive = [ "I'm really diggin'...", "I'm absolutely lovin'...", "I can't get enough of..."]
		negative = [ "I'd think about tweakin'...", "Not so sure I'm feelin'..."]
		
		positive_placeholder = random.choice(positive)
		negative_placeholder = random.choice(negative)


		model = ProjectMatch

		fields = [
		"user_a_positive_feedback",
		"user_a_negative_feedback",
		]

		labels = {
		"user_a_positive_feedback": _('What do you like?'),
		"user_a_negative_feedback": _('What would you change or add?'),
		}

		widgets = {
            'user_a_positive_feedback': Textarea(attrs={'cols': 60, 'rows': 5, 'placeholder': positive_placeholder}),
            'user_a_negative_feedback': Textarea(attrs={'cols': 60, 'rows': 5, 'placeholder': negative_placeholder}),
  
        }




class MatchFeedbackForm_B(forms.ModelForm):
	
	class Meta:

		positive = [ "I'm really diggin'...", "I'm absolutely lovin'...", "I can't get enough of..."]
		negative = [ "I'd think about tweakin'...", "Not so sure I'm feelin'..."]
		
		positive_placeholder = random.choice(positive)
		negative_placeholder = random.choice(negative)
		

		model = ProjectMatch

		fields = [
		"user_b_positive_feedback",
		"user_b_negative_feedback",
		]

		labels = {
		"user_b_positive_feedback": _('What do you like?'),
		"user_b_negative_feedback": _('What would you change or add?'),

		}

		widgets = {
            'user_b_positive_feedback': Textarea(attrs={'cols': 60, 'rows': 5, 'placeholder': positive_placeholder}),
            'user_b_negative_feedback': Textarea(attrs={'cols': 60, 'rows': 5, 'placeholder': negative_placeholder}),
        }






class ChatMessageForm(forms.ModelForm):

	class Meta:
		model = MatchChatMessage

		fields = [
		"message",
		]

		labels = {
		"message": _(''),
		}

		widgets = {
            'message': Textarea(attrs={'cols': 60, 'rows': 3}),
        }









class LikeForm_A(forms.ModelForm):
	class Meta:
		model = ProjectMatch
		fields = [
		"user_a_positive_feedback",
		"user_a_negative_feedback",
		]

		labels = {
		"user_a_positive_feedback": _('What do you like?'),
		"user_a_negative_feedback": _('What would you change or add?'),
		}

		widgets = {
            'user_a_positive_feedback': Textarea(attrs={'cols': 60, 'rows': 5}),
            'user_a_negative_feedback': Textarea(attrs={'cols': 60, 'rows': 5}),
        }


