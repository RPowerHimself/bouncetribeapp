# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0041_auto_20160517_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
