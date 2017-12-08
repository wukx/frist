# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0002_auto_20171208_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercategory',
            name='previous',
        ),
        migrations.AddField(
            model_name='exercategory',
            name='is_display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='exercategory',
            name='parent',
            field=models.ForeignKey(related_name='child', blank=True, to='onlineExam.ExerCategory', null=True),
        ),
        migrations.AddField(
            model_name='exercategory',
            name='sort',
            field=models.IntegerField(default=1),
        ),
    ]
