# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20151111_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_projects',
            field=models.IntegerField(default=0),
        ),
    ]
