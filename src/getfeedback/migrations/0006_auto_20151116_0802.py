# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getfeedback', '0005_useranswer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='their_answer_importance',
            new_name='their_importance',
        ),
    ]
