# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20151224_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.TextField(help_text=b'Lyrics, notes, or things to keep in mind.', max_length=300, blank=True),
        ),
    ]
