# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0025_auto_20151204_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='project_a_id',
        ),
    ]
