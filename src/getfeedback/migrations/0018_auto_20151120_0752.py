# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import getfeedback.models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0017_auto_20151120_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='audio_file',
            field=models.FileField(upload_to=getfeedback.models.audio_location, blank=True),
        ),
    ]
