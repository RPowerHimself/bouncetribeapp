# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_project_matched_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='matched_users',
            field=models.ManyToManyField(related_name='matched_users', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
