# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20160305_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=50, decimal_places=50, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=50, decimal_places=50, blank=True),
        ),
    ]
