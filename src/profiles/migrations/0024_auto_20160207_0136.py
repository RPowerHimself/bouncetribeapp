# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0015_auto_20160202_0512'),
        ('profiles', '0023_auto_20160204_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='active',
            new_name='unread',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='liker',
        ),
        migrations.AddField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(related_name='from_user', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(default=b'User Match', max_length=50, choices=[(b'User Match', b'User Match'), (b'Feedback Received', b'Feedback Received'), (b'Feedback Liked', b'Feedback Liked'), (b'Reviewer Promotion', b'Reviewer Promotion')]),
        ),
        migrations.AddField(
            model_name='notification',
            name='project',
            field=models.ForeignKey(to='projects.Project', null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(related_name='notified_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
