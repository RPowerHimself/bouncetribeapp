# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import tribe.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tribe', '0005_tribecomment_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TribeAudioInspiration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Track Title', max_length=50)),
                ('artist', models.CharField(default=b'Performer or Group', max_length=50)),
                ('link', models.CharField(default=b'YouTube URL', max_length=80)),
                ('artwork', models.ImageField(null=True, upload_to=tribe.models.upload_location, blank=True)),
                ('comments', models.TextField(default=b'Your thoughts', max_length=300, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
