# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0054_auto_20160606_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='featured_title',
            field=models.TextField(max_length=30, null=True, blank=True),
        ),
    ]
