# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tribe', '0011_tribeaudioinspiration_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='TribeFeedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inspiration', models.CharField(max_length=50)),
                ('item_type', models.CharField(default=b'Audio Inspiration', max_length=50, choices=[(b'Audio Project', b'Audio Project'), (b'Audio Inspiration', b'Audio Inspiration')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(to='tribe.TribeAudioProject')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
