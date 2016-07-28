# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import awesome_avatar.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20151217_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=awesome_avatar.fields.AvatarField(null=True, upload_to=b'avatars', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
