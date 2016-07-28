# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20160504_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='get_matched',
        ),
    ]
