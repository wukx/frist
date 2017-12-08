# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0008_auto_20171208_0444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercontent',
            old_name='type',
            new_name='style',
        ),
    ]
