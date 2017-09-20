# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'选手名称')
    SEX_CHOICES = (
        ('F', u'女'),
        ('M', u'男'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name=u'选手性别', default='M')
    age = models.IntegerField(verbose_name=u'年龄')
    height = models.IntegerField(verbose_name=u'身高')
    qq = models.IntegerField(verbose_name='QQ粉丝群')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"选手"


class Game(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'比赛名称')
    start_date = models.DateField(u'开始日期')
    end_date = models.DateField(u'结束日期')
    result = models.CharField(max_length=128, null=True, blank=True, verbose_name=u'比赛排名')
    champion = models.ForeignKey(Player, max_length=30, null=True,
                                 blank=True, verbose_name=u'冠军', related_name='champion')
    second_place = models.ForeignKey(
        Player, max_length=30, null=True, blank=True, verbose_name=u'亚军', related_name='second_place')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["start_date"]
        verbose_name_plural = u"比赛"


class Stage(models.Model):
    game = models.ForeignKey(Game, verbose_name=u'比赛名称')
    name = models.CharField(max_length=30, verbose_name=u'阶段名称')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"阶段"


class Group(models.Model):
    stage = models.ForeignKey(Stage, verbose_name=u'阶段名称')
    name = models.CharField(max_length=30, verbose_name=u'小组名称')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"小组"


class Battle(models.Model):
    group = models.ForeignKey(Group, verbose_name=u'小组名称')
    player1 = models.ForeignKey(Player, verbose_name=u'选手1', related_name='player1')
    player2 = models.ForeignKey(Player, verbose_name=u'选手2', related_name='player2')
    winner = models.ForeignKey(Player, null=True, blank=True,
                               verbose_name=u'胜者', related_name='winner')

    # def __unicode__(self):
    #     return self.name

    class Meta:
        verbose_name_plural = u"对抗"


class Match(models.Model):
    battle = models.ForeignKey(Battle, verbose_name=u'阶段名称')
    name = models.CharField(max_length=30, verbose_name=u'对战名称')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"对战"
