# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0018_subtribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtribe',
            old_name='user',
            new_name='leader',
        ),
    ]
