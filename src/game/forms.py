# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["name", "sex", "age", "height", "qq"]


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["name", "start_date", "end_date", "result", "champion", "second_place"]


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = ["game", "name"]


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["stage", "name"]


class BattleForm(ModelForm):
    class Meta:
        model = Battle
        fields = ["group", "player1", "player2", "winner"]


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ["battle", "name"]
