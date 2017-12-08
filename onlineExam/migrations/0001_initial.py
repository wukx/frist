# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExerCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name='\u7c7b\u522b\u540d\u79f0')),
                ('previous', models.ForeignKey(blank=True, to='onlineExam.ExerCategory', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name='\u9898\u76ee')),
                ('option', models.TextField(help_text='\u591a\u4e2a\u9009\u62e9\u9879\u7528~!!~\u5206\u5272', verbose_name='\u9009\u9879')),
                ('type', models.CharField(max_length=1, verbose_name='\u9898\u578b', choices=[(b'1', '\u5224\u65ad\u9898'), (b'2', '\u5355\u9009\u9898'), (b'3', '\u591a\u9009\u9898')])),
                ('answer', models.CharField(max_length=10, verbose_name='\u7b54\u6848')),
                ('addTime', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('modifyTime', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('linkExerCategory', models.ForeignKey(to='onlineExam.ExerCategory')),
            ],
        ),
    ]
