# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0005_exercontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercategory',
            name='parent',
        ),
    ]
