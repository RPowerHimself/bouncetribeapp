# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.validators
import image_cropping.fields
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_auto_20160204_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '200x200', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to=profiles.models.upload_location, validators=[profiles.validators.validate_file_size]),
        ),
    ]
