# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineExam', '0011_delete_exercontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sort', models.IntegerField(default=1)),
                ('is_display', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(related_name='child', blank=True, to='onlineExam.ExerCategory', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae')),
                ('option', models.TextField(help_text='\u591a\u4e2a\u9009\u62e9\u9879\u7528~!!~\u5206\u5272', verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9')),
                ('style', models.CharField(max_length=2, verbose_name=b'\xe9\xa2\x98\xe5\x9e\x8b', choices=[(b'1', b'\xe5\x88\xa4\xe6\x96\xad\xe9\xa2\x98'), (b'2', b'\xe5\x8d\x95\xe9\x80\x89\xe9\xa2\x98'), (b'3', b'\xe5\xa4\x9a\xe9\x80\x89\xe9\xa2\x98')])),
                ('answer', models.CharField(max_length=10, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('modifyTime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('linkExerCategory', models.ForeignKey(related_name='+', blank=True, to='onlineExam.ExerCategory', null=True)),
            ],
        ),
    ]
