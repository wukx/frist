# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0006_remove_exercategory_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercategory',
            name='parent',
            field=models.ForeignKey(related_name='child', blank=True, to='onlineExam.ExerCategory', null=True),
        ),
        migrations.AlterField(
            model_name='exercategory',
            name='title',
            field=models.CharField(max_length=80, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='exercontent',
            name='addTime',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='exercontent',
            name='answer',
            field=models.CharField(max_length=10, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88'),
        ),
        migrations.AlterField(
            model_name='exercontent',
            name='modifyTime',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='exercontent',
            name='option',
            field=models.TextField(help_text='\u591a\u4e2a\u9009\u62e9\u9879\u7528~!!~\u5206\u5272', verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9'),
        ),
        migrations.AlterField(
            model_name='exercontent',
            name='title',
            field=models.TextField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae'),
        ),
        migrations.AlterField(
            model_name='exercontent',
            name='type',
            field=models.CharField(max_length=2, verbose_name=b'\xe9\xa2\x98\xe5\x9e\x8b', choices=[(b'1', b'\xe5\x88\xa4\xe6\x96\xad\xe9\xa2\x98'), (b'2', b'\xe5\x8d\x95\xe9\x80\x89\xe9\xa2\x98'), (b'3', b'\xe5\xa4\x9a\xe9\x80\x89\xe9\xa2\x98')]),
        ),
    ]
