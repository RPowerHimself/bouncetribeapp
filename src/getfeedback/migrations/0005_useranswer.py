# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('getfeedback', '0004_auto_20151112_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('my_answer_importance', models.CharField(max_length=50, choices=[(b'Mandatory', b'Mandatory'), (b'Very Important', b'Very Important'), (b'Somewhat Important', b'Somewhat Important'), (b'Not Important', b'Not Important')])),
                ('their_answer_importance', models.CharField(max_length=50, choices=[(b'Mandatory', b'Mandatory'), (b'Very Important', b'Very Important'), (b'Somewhat Important', b'Somewhat Important'), (b'Not Important', b'Not Important')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(related_name='user_answer', to='getfeedback.Answer')),
                ('project', models.ForeignKey(to='getfeedback.Project')),
                ('their_answer', models.ForeignKey(related_name='match_answer', blank=True, to='getfeedback.Answer', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
