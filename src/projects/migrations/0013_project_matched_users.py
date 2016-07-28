# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0012_auto_20160124_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='matched_users',
            field=models.ManyToManyField(related_name='matched_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
