# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='user_a',
        ),
        migrations.RemoveField(
            model_name='match',
            name='user_b',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
