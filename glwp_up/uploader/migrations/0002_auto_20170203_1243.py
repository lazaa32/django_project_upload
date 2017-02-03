# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='pouser',
            new_name='user',
        ),
    ]
