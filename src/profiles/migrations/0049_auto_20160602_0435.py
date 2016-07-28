# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0048_auto_20160530_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influence',
            name='user',
            field=models.ManyToManyField(related_name='influence_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='user',
            field=models.ForeignKey(related_name='thumbail_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
