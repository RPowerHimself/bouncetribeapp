# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0004_tribeaudioproject_active'),
        ('profiles', '0032_auto_20160215_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='tribe_project',
            field=models.ForeignKey(blank=True, to='tribe.TribeAudioProject', null=True),
        ),
    ]
