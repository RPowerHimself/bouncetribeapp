# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('getfeedback', '0007_auto_20151117_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='project',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='my_answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='project',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='their_answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='active',
        ),
        migrations.RemoveField(
            model_name='project',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='project',
            name='text',
        ),
        migrations.AddField(
            model_name='project',
            name='genre',
            field=models.CharField(default=b'Alternative Rock', max_length=50, choices=[(b'Alternative Rock', b'Alternative Rock'), (b'Ambient', b'Ambient'), (b'Bluegrass', b'Bluegrass'), (b'Blues', b'Blues')]),
        ),
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.CharField(default=b'Beginner', max_length=50, choices=[(b'Beginner', b'Beginner'), (b'Experienced', b'Experienced'), (b'Seasoned', b'Seasoned')]),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default=b'ProjectTitle', max_length=120),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
