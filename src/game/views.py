# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Player, Game


def game(request):
    if request.method == 'GET':
        players = Player.objects.all()
        games = Player.objects.all()
        context = {
            "players": players,
            "games": games
        }
    elif request.method == 'POST':
        return render(request, "game.html")
    return render(request, "game.html", context=context)
