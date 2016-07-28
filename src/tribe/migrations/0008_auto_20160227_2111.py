# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0007_auto_20160227_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeaudioinspiration',
            name='item_type',
            field=models.CharField(default=b'Audio Inspiration', max_length=50, choices=[(b'Audio Project', b'Audio Project'), (b'Audio Inspiration', b'Audio Inspiration')]),
        ),
        migrations.AddField(
            model_name='tribeaudioproject',
            name='item_type',
            field=models.CharField(default=b'Audio Project', max_length=50, choices=[(b'Audio Project', b'Audio Project'), (b'Audio Inspiration', b'Audio Inspiration')]),
        ),
    ]
