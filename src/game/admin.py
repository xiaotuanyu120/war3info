# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Player, Game, Stage, Group, Battle, Match


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "sex", "age", "height", "qq")


class GameAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "result", "champion", "second_place")


class StageAdmin(admin.ModelAdmin):
    list_display = ("game", "name")


class GroupAdmin(admin.ModelAdmin):
    list_display = ("stage", "name")


class BattleAdmin(admin.ModelAdmin):
    list_display = ("group", "player1", "player2", "winner")


class MatchAdmin(admin.ModelAdmin):
    list_display = ("battle", "name")


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Battle, BattleAdmin)
admin.site.register(Match, MatchAdmin)
