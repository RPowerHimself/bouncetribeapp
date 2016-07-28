# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0052_auto_20160606_0521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='audio_file',
            new_name='featured_song',
        ),
    ]
