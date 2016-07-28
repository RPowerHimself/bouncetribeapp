# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import getfeedback.validators
import getfeedback.models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0018_auto_20151120_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='match_nearby',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='audio_file',
            field=models.FileField(blank=True, upload_to=getfeedback.models.audio_location, validators=[getfeedback.validators.validate_file_extension]),
        ),
    ]
