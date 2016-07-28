# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0008_auto_20160227_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tribeaudioinspiration',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='tribeaudioproject',
            options={'ordering': ['-created']},
        ),
    ]
