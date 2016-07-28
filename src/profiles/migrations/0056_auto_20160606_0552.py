# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0055_profile_featured_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='featured_title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
