# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_thumbnail_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'image', '430x360', hide_image_field=False, size_warning=False, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping'),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to=profiles.models.upload_location, blank=True),
        ),
    ]
