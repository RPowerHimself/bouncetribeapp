# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tribe', '0004_tribeaudioproject_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribecomment',
            name='project_user',
            field=models.ForeignKey(related_name='project_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
