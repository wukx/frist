# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0010_auto_20171208_0450'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExerContent',
        ),
    ]
