# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tribe.models
import tribe.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0006_tribeaudioinspiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeaudioinspiration',
            name='artist',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tribeaudioinspiration',
            name='artwork',
            field=models.ImageField(blank=True, null=True, upload_to=tribe.models.upload_location, validators=[tribe.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='tribeaudioinspiration',
            name='comments',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tribeaudioinspiration',
            name='link',
            field=models.CharField(default=b'https://', max_length=180),
        ),
        migrations.AlterField(
            model_name='tribeaudioinspiration',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
