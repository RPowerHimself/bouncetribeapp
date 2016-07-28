# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151209_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmatch',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
