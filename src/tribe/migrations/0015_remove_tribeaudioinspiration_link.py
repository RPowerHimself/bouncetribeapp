# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0014_auto_20160302_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tribeaudioinspiration',
            name='link',
        ),
    ]
