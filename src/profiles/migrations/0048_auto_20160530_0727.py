# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0047_notification_subtribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(default=b'User Match', max_length=50, choices=[(b'User Match', b'User Match'), (b'Feedback Received', b'Feedback Received'), (b'Feedback Liked', b'Feedback Liked'), (b'Reviewer Promotion', b'Reviewer Promotion'), (b'Tribe Request Accepted', b'Tribe Request Accepted'), (b'Tribe Feedback', b'Tribe Feedback'), (b'SubTribe Created', b'SubTribe Created')]),
        ),
    ]
