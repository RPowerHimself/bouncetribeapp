# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import tribe.models
import tribe.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TribeAudioProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b"Your Project's Title", unique=True, max_length=30)),
                ('genre', models.CharField(default=b'Alternative Rock', max_length=50, choices=[(b'Alternative Rock', b'Alternative Rock'), (b'Ambient', b'Ambient'), (b'Christian Rock', b'Christian Rock'), (b'Christian Gospel', b'Christian Gospel'), (b'Classical', b'Classical'), (b'Comedy', b'Comedy'), (b'Country', b'Country'), (b'Dance & EDM', b'Dance & EDM'), (b'Deep House', b'Deep House'), (b'Disco', b'Disco'), (b'Dubstep', b'Dubstep'), (b'Electronic', b'Electronic'), (b'Folk', b'Folk'), (b'Funk', b'Funk'), (b'Hip Hop & Rap', b'Hip Hop & Rap'), (b'House', b'House'), (b'Indie', b'Indie'), (b'Instrumental', b'Instrumental'), (b'Jazz', b'Jazz'), (b'Metal', b'Metal'), (b'Pop', b'Pop'), (b'Pop Rock', b'Pop Rock'), (b'R&B Soul', b'R&B Soul'), (b'Reggae', b'Reggae'), (b'Rock', b'Rock'), (b'Ska', b'Ska'), (b'Singer-Songwriter', b'Singer-Songwriter'), (b'Soundtrack', b'Soundtrack'), (b'Techno', b'Techno'), (b'Trance', b'Trance'), (b'Trap', b'Trap'), (b'Trip Hop', b'Trip Hop'), (b'World', b'World'), (b'Other', b'Other')])),
                ('audio_file', models.FileField(blank=True, upload_to=tribe.models.audio_location, validators=[tribe.validators.validate_file_extension])),
                ('short_description', models.TextField(help_text=b'Lyrics, notes, or things to keep in mind.', max_length=300, blank=True)),
                ('incomplete', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
