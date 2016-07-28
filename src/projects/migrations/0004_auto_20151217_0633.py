# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectmatch_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmatch',
            name='user_a_negative_feedback',
            field=models.TextField(default=b'Waiting for Feedback', max_length=600, null=True, help_text=b'Please be constructive.', blank=True),
        ),
        migrations.AddField(
            model_name='projectmatch',
            name='user_a_positive_feedback',
            field=models.TextField(default=b'Waiting for Feedback', max_length=600, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projectmatch',
            name='user_b_negative_feedback',
            field=models.TextField(default=b'Waiting for Feedback', max_length=600, null=True, help_text=b'Please be constructive.', blank=True),
        ),
        migrations.AddField(
            model_name='projectmatch',
            name='user_b_positive_feedback',
            field=models.TextField(default=b'Waiting for Feedback', max_length=600, null=True, blank=True),
        ),
    ]
