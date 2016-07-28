# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_remove_project_get_matched'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='incomplete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default=b'My Project', unique=True, max_length=30),
        ),
    ]
