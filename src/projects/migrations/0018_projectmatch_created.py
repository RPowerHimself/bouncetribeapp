# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_project_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmatch',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
