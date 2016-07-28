from django import forms

from .models import GetFeedbackProject


class GetFeedbackProjectForm(forms.ModelForm):
	class Meta:
		model = GetFeedbackProject
		fields = [
		"title",
		"genre",
		"skill",
		]











# class ContactForm(forms.Form):
# 	name = forms.CharField(max_length=120, required=False)
# 	email = forms.EmailField(required=True, help_text='A valid email address, please.')
# 	comment = forms.CharField(required=True, widget=forms.Textarea)






