# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20160306_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='genre',
            field=models.CharField(default=b'EDM & Electronic', max_length=50, choices=[(b'Christian & Gospel', b'Christian & Gospel'), (b'Classical', b'Classical'), (b'Country', b'Country'), (b'EDM & Electronic', b'EDM & Electronic'), (b'Folk', b'Folk'), (b'Hip Hop & Rap', b'Hip Hop & Rap'), (b'Instrumental', b'Instrumental'), (b'Jazz', b'Jazz'), (b'Metal', b'Metal'), (b'Pop', b'Pop'), (b'Pop Rock', b'Pop Rock'), (b'R&B Soul', b'R&B Soul'), (b'Hard Rock', b'Hard Rock'), (b'Singer-Songwriter', b'Singer-Songwriter'), (b'Other', b'Other (Please Describe)')]),
        ),
        migrations.AlterField(
            model_name='tribeproject',
            name='genre',
            field=models.CharField(default=b'Alternative Rock', max_length=50, choices=[(b'Christian & Gospel', b'Christian & Gospel'), (b'Classical', b'Classical'), (b'Country', b'Country'), (b'EDM & Electronic', b'EDM & Electronic'), (b'Folk', b'Folk'), (b'Hip Hop & Rap', b'Hip Hop & Rap'), (b'Instrumental', b'Instrumental'), (b'Jazz', b'Jazz'), (b'Metal', b'Metal'), (b'Pop', b'Pop'), (b'Pop Rock', b'Pop Rock'), (b'R&B Soul', b'R&B Soul'), (b'Hard Rock', b'Hard Rock'), (b'Singer-Songwriter', b'Singer-Songwriter'), (b'Other', b'Other (Please Describe)')]),
        ),
    ]
