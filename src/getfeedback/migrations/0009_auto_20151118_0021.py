# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0008_auto_20151117_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='genre',
            field=models.CharField(default=b'Alternative Rock', max_length=50, choices=[(b'Alternative Rock', b'Alternative Rock'), (b'Ambient', b'Ambient'), (b'Bluegrass', b'Bluegrass'), (b'Blues', b'Blues'), (b'Childrens', b'Childrens'), (b'Bluegrass', b'Bluegrass'), (b'Christian Rock', b'Christian Rock'), (b'Christian Gospel', b'Christian Gospel'), (b'Classical', b'Classical'), (b'Comedy', b'Comedy'), (b'Country', b'Country'), (b'Dance & EDM', b'Dance & EDM'), (b'Dancehall', b'Dancehall'), (b'Deep House', b'Deep House'), (b'Disco', b'Disco'), (b'Drum & Bass', b'Drum & Bass')]),
        ),
    ]
