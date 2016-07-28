# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0002_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='answers',
            field=models.ManyToManyField(to='getfeedback.Answer'),
        ),
    ]
