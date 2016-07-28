# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_auto_20160602_0435'),
        ('profiles', '0057_auto_20160612_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='featured_title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='featured_track',
        ),
        migrations.AddField(
            model_name='profile',
            name='featured_project',
            field=models.ForeignKey(related_name='featured_project', blank=True, to='projects.Project', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_project',
            field=models.ForeignKey(related_name='current_project', blank=True, to='projects.Project', null=True),
        ),
    ]
