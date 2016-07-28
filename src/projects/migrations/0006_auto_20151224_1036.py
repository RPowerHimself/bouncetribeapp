# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20151217_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmatch',
            name='user_a_like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectmatch',
            name='user_b_like',
            field=models.BooleanField(default=False),
        ),
    ]
