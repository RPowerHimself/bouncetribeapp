# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_auto_20160207_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='project',
            field=models.ForeignKey(blank=True, to='projects.Project', null=True),
        ),
    ]
