# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_auto_20160526_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchchatmessage',
            name='to_user',
            field=models.ForeignKey(related_name='message_to_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='matchchatmessage',
            name='user',
            field=models.ForeignKey(related_name='message_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(related_name='project_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
