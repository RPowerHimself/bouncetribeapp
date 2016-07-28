# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20160305_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.DecimalField(default=0, max_digits=30, decimal_places=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.DecimalField(default=0, max_digits=30, decimal_places=30),
        ),
    ]
