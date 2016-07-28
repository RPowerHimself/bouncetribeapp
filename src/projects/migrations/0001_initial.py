# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import projects.models
import projects.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b"Your Project's Title", max_length=120)),
                ('genre', models.CharField(default=b'Alternative Rock', max_length=50, choices=[(b'Alternative Rock', b'Alternative Rock'), (b'Ambient', b'Ambient'), (b'Christian Rock', b'Christian Rock'), (b'Christian Gospel', b'Christian Gospel'), (b'Classical', b'Classical'), (b'Comedy', b'Comedy'), (b'Country', b'Country'), (b'Dance & EDM', b'Dance & EDM'), (b'Deep House', b'Deep House'), (b'Disco', b'Disco'), (b'Dubstep', b'Dubstep'), (b'Electronic', b'Electronic'), (b'Folk', b'Folk'), (b'Funk', b'Funk'), (b'Hip Hop & Rap', b'Hip Hop & Rap'), (b'House', b'House'), (b'Indie', b'Indie'), (b'Instrumental', b'Instrumental'), (b'Jazz', b'Jazz'), (b'Metal', b'Metal'), (b'Pop', b'Pop'), (b'Pop Rock', b'Pop Rock'), (b'R&B Soul', b'R&B Soul'), (b'Reggae', b'Reggae'), (b'Rock', b'Rock'), (b'Ska', b'Ska'), (b'Singer-Songwriter', b'Singer-Songwriter'), (b'Soundtrack', b'Soundtrack'), (b'Techno', b'Techno'), (b'Trance', b'Trance'), (b'Trap', b'Trap'), (b'Trip Hop', b'Trip Hop'), (b'World', b'World'), (b'Other', b'Other')])),
                ('experience', models.CharField(default=b'Novice', max_length=50, choices=[(b'Novice', b'Novice (Just Started)'), (b'Beginner', b'Beginner (0-2 Years)'), (b'Skilled', b'Skilled (3-5 Years)'), (b'Seasoned', b'Seasoned (6+ Years)')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('queued', models.BooleanField(default=True)),
                ('audio_file', models.FileField(blank=True, upload_to=projects.models.audio_location, validators=[projects.validators.validate_file_extension])),
                ('match_nearby', models.BooleanField(default=True)),
                ('short_description', models.TextField(help_text=b'Anything we should know?', max_length=300, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project_a', models.ForeignKey(related_name='project_a_id', to='projects.Project')),
                ('project_b', models.ForeignKey(related_name='project_b_id', to='projects.Project')),
                ('user_a', models.ForeignKey(related_name='match_user_a', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.ForeignKey(related_name='match_user_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
