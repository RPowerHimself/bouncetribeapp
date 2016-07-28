# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0009_auto_20160227_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeaudioinspiration',
            name='link',
            field=models.CharField(max_length=180),
        ),
    ]
