# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Player, Game, Stage, Group, Battle, Match


class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
