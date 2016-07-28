# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0023_auto_20151121_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.TextField(default=2, help_text=b'Anything we should know?', max_length=300),
            preserve_default=False,
        ),
    ]
