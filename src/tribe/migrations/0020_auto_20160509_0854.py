# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0019_auto_20160509_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtribe',
            name='members',
            field=models.ManyToManyField(related_name='tribe_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
