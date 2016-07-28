# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import audiofield.fields
import getfeedback.models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0015_auto_20151119_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='audio_file',
            field=audiofield.fields.AudioField(help_text=b'Allowed type - .mp3, .wav, .ogg', upload_to=getfeedback.models.audio_location, blank=True),
        ),
    ]
