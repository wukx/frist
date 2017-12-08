# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
Q_TYPE_CHOICES = (
    ("1", "判断题"),
    ("2", "单选题"),
    ("3", "多选题"),
)


class ExerCategory(models.Model):
    title = models.CharField(verbose_name="类别名称", max_length=80)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child')
    sort = models.IntegerField(default=1)
    is_display = models.BooleanField(default=True)

    def __unicode__(self):
        return self


class ExerContent(models.Model):
    title = models.TextField(verbose_name='题目')
    option = models.TextField(verbose_name='选项', help_text=u"多个选择项用~!!~分割")
    style = models.CharField(verbose_name='题型', choices=Q_TYPE_CHOICES, max_length=2)
    answer = models.CharField(verbose_name="答案", max_length=10)
    addTime = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    modifyTime = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)
    linkExerCategory = models.ForeignKey(ExerCategory, null=True, blank=True, related_name='+')


