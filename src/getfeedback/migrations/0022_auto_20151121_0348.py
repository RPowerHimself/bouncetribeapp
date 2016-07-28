# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0021_auto_20151121_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='genre',
            field=models.CharField(default=b'Alternative Rock', max_length=50, choices=[(b'Alternative Rock', b'Alternative Rock'), (b'Ambient', b'Ambient'), (b'Blues', b'Blues'), (b'Bluegrass', b'Bluegrass'), (b'Christian Rock', b'Christian Rock'), (b'Christian Gospel', b'Christian Gospel'), (b'Classical', b'Classical'), (b'Comedy', b'Comedy'), (b'Country', b'Country'), (b'Dance & EDM', b'Dance & EDM'), (b'Deep House', b'Deep House'), (b'Disco', b'Disco'), (b'Dubstep', b'Dubstep'), (b'Electronic', b'Electronic'), (b'Folk', b'Folk'), (b'Funk', b'Funk'), (b'Hip Hop & Rap', b'Hip Hop & Rap'), (b'House', b'House'), (b'Indie', b'Indie'), (b'Instrumental', b'Instrumental'), (b'Jazz', b'Jazz'), (b'Metal', b'Metal'), (b'Pop', b'Pop'), (b'Pop Rock', b'Pop Rock'), (b'R&B Soul', b'R&B Soul'), (b'Reggae', b'Reggae'), (b'Rock', b'Rock'), (b'Ska', b'Ska'), (b'Singer-Songwriter', b'Singer-Songwriter'), (b'Soundtrack', b'Soundtrack'), (b'Techno', b'Techno'), (b'Trance', b'Trance'), (b'Trap', b'Trap'), (b'Trip Hop', b'Trip Hop'), (b'World', b'World'), (b'Other', b'Other')]),
        ),
    ]
