# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_total_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_projects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
    ]
