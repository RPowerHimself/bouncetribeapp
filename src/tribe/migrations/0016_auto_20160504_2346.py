# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0015_remove_tribeaudioinspiration_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribecomment',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
    ]
