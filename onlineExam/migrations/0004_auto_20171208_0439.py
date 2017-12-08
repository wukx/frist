# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0003_auto_20171208_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercontent',
            name='linkExerCategory',
        ),
        migrations.DeleteModel(
            name='ExerContent',
        ),
    ]
