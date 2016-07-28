# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0056_auto_20160606_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.CharField(default=b'Beginner (0-2 Years)', max_length=50, choices=[(b'Novice (Just Started)', b'Novice (Just Started)'), (b'Beginner (0-2 Years)', b'Beginner (0-2 Years)'), (b'Skilled (3-9 Years)', b'Skilled (3-9 Years)'), (b'Accomplished (10-24 Years)', b'Accomplished (10-24 Years)'), (b'Veteran (25+ Years)', b'Veteran (25+ Years)')]),
        ),
    ]
