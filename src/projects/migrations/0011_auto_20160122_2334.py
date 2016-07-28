# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160121_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmatch',
            name='user_a_negative_feedback',
            field=models.TextField(help_text=b'Please be constructive.', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projectmatch',
            name='user_a_positive_feedback',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projectmatch',
            name='user_b_negative_feedback',
            field=models.TextField(help_text=b'Please be constructive.', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='projectmatch',
            name='user_b_positive_feedback',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
