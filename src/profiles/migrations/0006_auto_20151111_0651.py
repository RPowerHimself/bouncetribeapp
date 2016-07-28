# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=b'Tell us about yourself..', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'videos/', blank=True),
        ),
    ]
