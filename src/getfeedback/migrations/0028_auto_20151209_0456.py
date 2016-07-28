# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('getfeedback', '0027_auto_20151206_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project_a', models.ForeignKey(related_name='project_a_id', to='getfeedback.Project')),
                ('project_b', models.ForeignKey(related_name='project_b_id', to='getfeedback.Project')),
                ('user_a', models.ForeignKey(related_name='match_user_a', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.ForeignKey(related_name='match_user_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='user_a',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
