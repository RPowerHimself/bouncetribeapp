# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0002_tribecomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tribecomment',
            name='text',
        ),
        migrations.AddField(
            model_name='tribecomment',
            name='negative_feedback',
            field=models.TextField(max_length=600, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tribecomment',
            name='positive_feedback',
            field=models.TextField(max_length=600, null=True, blank=True),
        ),
    ]
