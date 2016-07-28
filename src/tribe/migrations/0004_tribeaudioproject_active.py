# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0003_auto_20160213_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeaudioproject',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
