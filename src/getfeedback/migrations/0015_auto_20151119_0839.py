# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0014_auto_20151118_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='queued',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='skill',
            field=models.CharField(default=b'Beginner', max_length=50, choices=[(b'Beginner', b'Beginner (Just Started)'), (b'Experienced', b'Experienced (1-3 Years)'), (b'Seasoned', b'Seasoned (4+ Years)')]),
        ),
    ]
