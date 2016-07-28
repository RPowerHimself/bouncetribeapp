# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positive_feedback', models.TextField(max_length=120)),
                ('negative_feedback', models.TextField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('feedbacker', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
