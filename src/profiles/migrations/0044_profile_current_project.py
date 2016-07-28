# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_remove_project_experience'),
        ('profiles', '0043_auto_20160518_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_project',
            field=models.ForeignKey(related_name='current_projects', to='projects.Project', null=True),
        ),
    ]
