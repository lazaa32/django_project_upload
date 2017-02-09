# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uploader.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_auto_20170208_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='expire_date',
            field=models.DateTimeField(default=uploader.models.expire),
        ),
    ]
