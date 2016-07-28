# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0010_auto_20160301_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeaudioinspiration',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True, blank=True),
        ),
    ]
