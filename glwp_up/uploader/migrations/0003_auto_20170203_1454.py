# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uploader.formatChecker
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20170203_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 17, 13, 54, 26, 330571, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_file',
            field=uploader.formatChecker.ContentTypeRestrictedFileField(upload_to=b'./uploaded_projects', null=True, verbose_name=b'Project file'),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
    ]
