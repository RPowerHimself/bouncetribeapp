# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0021_auto_20160509_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtribe',
            name='leader',
            field=models.ForeignKey(related_name='subtribe_leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subtribe',
            name='members',
            field=models.ManyToManyField(related_name='subtribe_members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tribeaudioinspiration',
            name='user',
            field=models.ForeignKey(related_name='inspiration_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tribeaudioproject',
            name='user',
            field=models.ForeignKey(related_name='tribe_project_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tribecomment',
            name='project',
            field=models.ForeignKey(related_name='comment_project', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='tribecomment',
            name='project_user',
            field=models.ForeignKey(related_name='comment_project_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='tribecomment',
            name='user',
            field=models.ForeignKey(related_name='comment_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tribefeeditem',
            name='inspiration',
            field=models.ForeignKey(related_name='feed_item_inspiration', blank=True, to='tribe.TribeAudioInspiration', null=True),
        ),
        migrations.AlterField(
            model_name='tribefeeditem',
            name='project',
            field=models.ForeignKey(related_name='feed_item_project', blank=True, to='projects.Project', null=True),
        ),
        migrations.AlterField(
            model_name='tribefeeditem',
            name='user',
            field=models.ForeignKey(related_name='feed_item_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
