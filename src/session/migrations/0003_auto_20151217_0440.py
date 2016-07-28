# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_auto_20151125_0655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionfeedback',
            name='feedbacker',
        ),
        migrations.RemoveField(
            model_name='sessionfeedback',
            name='negative_feedback',
        ),
        migrations.RemoveField(
            model_name='sessionfeedback',
            name='positive_feedback',
        ),
        migrations.AddField(
            model_name='sessionfeedback',
            name='user_a_negative_feedback',
            field=models.TextField(help_text=b'Please be constructive.', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sessionfeedback',
            name='user_a_positive_feedback',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sessionfeedback',
            name='user_b_negative_feedback',
            field=models.TextField(help_text=b'Please be constructive.', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sessionfeedback',
            name='user_b_positive_feedback',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
