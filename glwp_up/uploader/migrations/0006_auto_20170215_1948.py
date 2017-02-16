# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uploader.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0005_auto_20170215_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_file',
            field=models.FileField(upload_to=uploader.models.get_file_path, null=True, verbose_name=b'Project file'),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_name',
            field=models.CharField(default=b'ProjectName', unique=True, max_length=40, verbose_name=b'Project name'),
        ),
    ]
