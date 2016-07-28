# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0039_auto_20160517_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.CharField(default=b'Beginner', max_length=50, choices=[(b'Complete Novice (Just Started)', b'Complete Novice (Just Started)'), (b'Beginner', b'Beginner (0-2 Years)'), (b'Skilled', b'Skilled (3-5 Years)'), (b'Seasoned', b'Seasoned (6+ Years)')]),
        ),
    ]
