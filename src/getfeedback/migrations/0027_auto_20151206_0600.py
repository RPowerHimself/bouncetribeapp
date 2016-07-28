# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0026_remove_match_project_a_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='user_b',
        ),
        migrations.AlterField(
            model_name='match',
            name='user_a',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
