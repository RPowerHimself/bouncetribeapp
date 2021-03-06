# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160128_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='experience',
            field=models.CharField(default=b'Novice', max_length=50, choices=[(b'Novice (Just Started)', b'Novice (Just Started)'), (b'Beginner (0-2 Years)', b'Beginner (0-2 Years)'), (b'Skilled (3-5 Years)', b'Skilled (3-5 Years)'), (b'Seasoned (6+ Years)', b'Seasoned (6+ Years)')]),
        ),
    ]
