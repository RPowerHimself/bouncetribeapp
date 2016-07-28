# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionfeedback',
            name='negative_feedback',
            field=models.TextField(help_text=b'Please be constructive.', max_length=500),
        ),
        migrations.AlterField(
            model_name='sessionfeedback',
            name='positive_feedback',
            field=models.TextField(max_length=500),
        ),
    ]
