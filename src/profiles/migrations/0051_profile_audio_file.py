# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.validators
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0050_auto_20160602_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='audio_file',
            field=models.FileField(blank=True, upload_to=profiles.models.audio_location, validators=[profiles.validators.validate_file_extension]),
        ),
    ]
