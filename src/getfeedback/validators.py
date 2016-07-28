from django.conf import settings
from django.core.exceptions import ValidationError



def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.wave']
    if not ext in valid_extensions:
        raise ValidationError(u'Please upload .mp3 or .wav files.')