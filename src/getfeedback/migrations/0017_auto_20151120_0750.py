# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import audiofield.fields
import getfeedback.models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0016_project_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='audio_file',
            field=audiofield.fields.AudioField(upload_to=getfeedback.models.audio_location, blank=True),
        ),
    ]
