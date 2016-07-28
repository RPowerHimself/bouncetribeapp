# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_profile_influences'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.CharField(default=b'User Match', max_length=120, choices=[(b'New Reviewer', b'New Reviewer'), (b'Liked Reviewer', b'Liked Reviewer'), (b'Helpful Reviewer', b'Helpful Reviewer'), (b'Reviewer Promotion', b'Reviewer Promotion'), (b'Respected Reviewer', b'Respected Reviewer'), (b'Revered Reviewer', b'Revered Reviewer'), (b'Top Reviewer', b'Top Reviewer')]),
        ),
    ]
