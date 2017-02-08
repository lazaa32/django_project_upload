# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20170208_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 17, 35, 44, 424074, tzinfo=utc)),
        ),
    ]
