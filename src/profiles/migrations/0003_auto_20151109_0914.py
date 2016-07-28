# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
