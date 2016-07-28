# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0003_auto_20151112_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='project',
            field=models.ForeignKey(default=1, to='getfeedback.Project'),
            preserve_default=False,
        ),
    ]
