# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_auto_20160207_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notification_type',
        ),
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(default=b'User Match', max_length=50, choices=[(b'User Match', b'User Match'), (b'Feedback Received', b'Feedback Received'), (b'Feedback Liked', b'Feedback Liked'), (b'Reviewer Promotion', b'Reviewer Promotion')]),
        ),
    ]
