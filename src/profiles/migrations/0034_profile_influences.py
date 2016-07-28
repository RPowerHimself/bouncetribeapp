# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0033_notification_tribe_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='influences',
            field=models.TextField(max_length=600, null=True, blank=True),
        ),
    ]
