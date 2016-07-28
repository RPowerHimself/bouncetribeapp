# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0013_auto_20160301_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribefeeditem',
            name='inspiration',
            field=models.ForeignKey(blank=True, to='tribe.TribeAudioInspiration', null=True),
        ),
        migrations.AlterField(
            model_name='tribefeeditem',
            name='project',
            field=models.ForeignKey(blank=True, to='tribe.TribeAudioProject', null=True),
        ),
    ]
