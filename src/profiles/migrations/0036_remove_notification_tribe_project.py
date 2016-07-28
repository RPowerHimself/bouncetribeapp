# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0035_profile_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='tribe_project',
        ),
    ]
