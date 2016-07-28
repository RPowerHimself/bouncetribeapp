# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_projectmatch_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmatch',
            name='created',
        ),
    ]
