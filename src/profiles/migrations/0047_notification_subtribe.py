# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0046_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='subtribe',
            field=models.ForeignKey(blank=True, to='profiles.MySubTribe', null=True),
        ),
    ]
