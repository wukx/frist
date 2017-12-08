# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0009_auto_20171208_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='exercontent',
            name='linkExerCategory',
        ),
        migrations.DeleteModel(
            name='ExerCategory',
        ),
    ]
