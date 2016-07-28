# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0029_auto_20160211_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='session',
            field=models.ForeignKey(blank=True, to='projects.ProjectMatch', null=True),
        ),
    ]
