# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0020_auto_20160509_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtribe',
            name='leader',
            field=models.ForeignKey(related_name='leader', to=settings.AUTH_USER_MODEL),
        ),
    ]
