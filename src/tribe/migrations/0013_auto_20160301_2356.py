# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0012_tribefeeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribefeeditem',
            name='inspiration',
            field=models.ForeignKey(to='tribe.TribeAudioInspiration'),
        ),
    ]
