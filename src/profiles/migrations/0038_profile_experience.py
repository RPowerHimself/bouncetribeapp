# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0037_mysubtribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.CharField(default=b'Novice', max_length=50, choices=[(b'Novice', b'Complete Novice (Just Started)'), (b'Beginner', b'Beginner (0-2 Years)'), (b'Skilled', b'Skilled (3-5 Years)'), (b'Seasoned', b'Seasoned (6+ Years)')]),
        ),
    ]
