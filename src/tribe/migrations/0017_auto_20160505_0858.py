# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0016_auto_20160504_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribefeeditem',
            name='project',
            field=models.ForeignKey(blank=True, to='projects.Project', null=True),
        ),
    ]
