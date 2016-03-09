# coding=utf-8
from __future__ import unicode_literals
from django.db import IntegrityError
from models import Magazine, Game, Patch
from magazines.igromania.includes.getters import get_games_2000_all, get_patches_2000


def fill_magazine(request):
    """
    добавляет в базу существующие выпуски журнала

    :param request:
    """
    current_year = 1997
    current_month = 10

    for item in range(1, 223):
        Magazine(number=item, public_year=current_year, public_month=current_month).save()
        current_month += 1
        if current_month % 13 == 0:
            current_month = 1
            current_year += 1


def fill_games(request):
    """
    добавляет в базу игры из выпуска

    :param request:
    """
    for item in get_games_2000_all():
        print(item)
        try:
            Game(title=item).save()
        except IntegrityError, e:
            print(item + 'уже есть', e)


def fill_patches(request):
    """
    добавляет в базу инфу по патчам из выпуска

    :param request:
    """
    games = sorted(get_patches_2000()[0])
    patches = get_patches_2000()[1]

    games_qset = []
    for item in Game.objects.all():
        if item.title in games:
            games_qset.append(item)

    for i, item in enumerate(games):
        print(games_qset[i])

        Patch(magazine_id=28, game_id=int(games_qset[i].id), version=patches[i][1][1],
              description=patches[i][3][1]).save()
