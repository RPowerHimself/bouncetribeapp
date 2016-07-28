# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0019_auto_20151120_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='skill',
        ),
        migrations.AddField(
            model_name='project',
            name='experience',
            field=models.CharField(default=b'Beginner', max_length=50, choices=[(b'Novice', b'Novice (Just Started)'), (b'Beginner', b'Beginner (0-2 Years'), (b'Skilled', b'Skilled (3-5 Years)'), (b'Seasoned', b'Seasoned (6+ Years)')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default=b"Your Project's Title", max_length=120),
        ),
    ]
