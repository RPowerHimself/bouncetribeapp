# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_auto_20160108_0531'),
        ('profiles', '0015_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='liker',
            field=models.ForeignKey(related_name='liker', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='session',
            field=models.ForeignKey(to='projects.ProjectMatch', null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(related_name='notification_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
