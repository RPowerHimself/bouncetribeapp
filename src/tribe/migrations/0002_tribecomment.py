# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tribe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TribeComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=300, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(to='tribe.TribeAudioProject')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
