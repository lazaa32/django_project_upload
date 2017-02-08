# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 17, 33, 51, 62466, tzinfo=utc)),
        ),
    ]
