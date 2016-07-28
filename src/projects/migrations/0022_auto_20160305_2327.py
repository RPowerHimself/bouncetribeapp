# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20160222_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='latitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='longitude',
            field=models.IntegerField(default=0),
        ),
    ]
