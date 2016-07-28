# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0040_auto_20160517_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.CharField(default=b'Beginner (0-2 Years)', max_length=50, choices=[(b'Complete Novice (Just Started)', b'Complete Novice (Just Started)'), (b'Beginner (0-2 Years)', b'Beginner (0-2 Years)'), (b'Skilled (3-5 Years)', b'Skilled (3-5 Years)'), (b'Seasoned (6+ Years)', b'Seasoned (6+ Years)')]),
        ),
    ]
