# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('getfeedback', '0024_project_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.TextField(help_text=b'Anything we should know?', max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='project_a_id',
            field=models.ForeignKey(to='getfeedback.Project'),
        ),
        migrations.AddField(
            model_name='match',
            name='user_a',
            field=models.ForeignKey(related_name='match_user_a', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='user_b',
            field=models.ForeignKey(related_name='match_user_b', to=settings.AUTH_USER_MODEL),
        ),
    ]
