# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'比赛名称')
    start_date = models.DateField(u'开始日期')
    end_date = models.DateField(u'结束日期')
    result = models.CharField(max_length=128, verbose_name=u'比赛排名')
    champion = models.CharField(max_length=30, verbose_name=u'冠军')
    second_place = models.CharField(max_length=30, verbose_name=u'亚军')


class Battle(models.Model):
    game = models.ForeignKey(Game, verbose_name=u'比赛名称')
