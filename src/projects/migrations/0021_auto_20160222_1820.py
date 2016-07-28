# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0020_matchchatmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchchatmessage',
            name='other_user',
        ),
        migrations.AddField(
            model_name='matchchatmessage',
            name='to_user',
            field=models.ForeignKey(related_name='to_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
