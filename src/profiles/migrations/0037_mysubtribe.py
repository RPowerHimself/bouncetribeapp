# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0036_remove_notification_tribe_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySubTribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('leader', models.ForeignKey(related_name='tribe_leader', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='subtribe_members', to='profiles.Profile')),
            ],
        ),
    ]
