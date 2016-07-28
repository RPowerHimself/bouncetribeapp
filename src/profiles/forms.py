from django import forms
from profiles.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea
from image_cropping import ImageCropWidget

from awesome_avatar import forms as avatar_forms


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
		"experience",
		"location",
		"bio",
		"influences",
		"website",
		"email",
		"featured_project",
		]


		labels = {
		'picture': _('Profile Photo'),
		'location': _('City'),
		'bio': _('Your Bio'),
		'influences': _('Your Influences'),
		}


		widgets = {
            'bio': Textarea(attrs={'cols': 80, 'rows': 5}),
            'influences': Textarea(attrs={'cols': 80, 'rows': 5}),
            'email': forms.TextInput(attrs={'placeholder': 'john@gmail.com'}),
            'website': forms.TextInput(attrs={'placeholder': 'http://'}),

        }


class ProfilePhotoForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
		"image",
		"cropping",
		]

		labels = {
		'image': _('Your Photo'),
		'cropping': _('Crop Your Photo'),
		}



class ProfileNoPhotoForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = [
		"image",
		]


		labels = {
		'image': _('Choose Your Photo'),
		}











