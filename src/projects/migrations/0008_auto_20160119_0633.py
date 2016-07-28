# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160108_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='match_nearby',
            field=models.BooleanField(default=False),
        ),
    ]
