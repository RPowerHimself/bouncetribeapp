# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.validators
import profiles.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0049_auto_20160602_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySubTribeProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b"Your Project's Title", unique=True, max_length=30)),
                ('audio_file', models.FileField(blank=True, upload_to=profiles.models.audio_location, validators=[profiles.validators.validate_file_extension])),
                ('short_description', models.TextField(help_text=b'Lyrics, notes, or things to keep in mind.', max_length=300, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='mysubtribe',
            name='leader',
            field=models.ForeignKey(related_name='my_subtribe_leader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mysubtribe',
            name='members',
            field=models.ManyToManyField(related_name='my_subtribe_members', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='mysubtribeproject',
            name='subtribe',
            field=models.ForeignKey(related_name='my_subtribe', to='profiles.MySubTribe'),
        ),
        migrations.AddField(
            model_name='mysubtribeproject',
            name='user',
            field=models.ForeignKey(related_name='subtribe_project_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
