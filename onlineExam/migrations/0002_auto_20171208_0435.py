# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercontent',
            name='linkExerCategory',
            field=models.ForeignKey(related_name='+', to='onlineExam.ExerCategory'),
        ),
    ]
