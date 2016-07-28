from django.conf import settings
from django.core.exceptions import ValidationError



def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.wave']
    filesize = value.file.size
    megabyte_limit = 15

    if filesize > megabyte_limit*1024*1024:
    	raise ValidationError("The maximum file size is %sMB" % str(megabyte_limit))

    if not ext in valid_extensions:
        raise ValidationError(u'Please upload .mp3 or .wav files.')



def validate_file_size(value):
    import os
    filesize = value.file.size
    megabyte_limit = 10

    if filesize > megabyte_limit*1024*1024:
    	raise ValidationError("The maximum file size is %sMB" % str(megabyte_limit))