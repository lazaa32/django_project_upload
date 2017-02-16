# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0006_auto_20170215_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_file',
            field=models.FileField(upload_to=b'./uploaded_projects', null=True, verbose_name=b'Project file'),
        ),
    ]
