# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20160204_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=image_cropping.fields.ImageCropField(upload_to=profiles.models.upload_location, blank=True),
        ),
    ]
