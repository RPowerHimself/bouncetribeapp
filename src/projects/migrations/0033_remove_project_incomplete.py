# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_remove_project_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='incomplete',
        ),
    ]
