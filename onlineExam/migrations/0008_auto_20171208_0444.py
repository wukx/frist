# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0007_auto_20171208_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercontent',
            name='linkExerCategory',
            field=models.ForeignKey(related_name='+', blank=True, to='onlineExam.ExerCategory', null=True),
        ),
    ]
