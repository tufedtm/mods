# coding=utf-8
from __future__ import unicode_literals
from pprint import pprint
from django.db import IntegrityError
from . import models
from magazines.igromania.includes.getters import get_games_2000_all, get_patches_2000, get_demos_2000
from magazines.igromania.includes.getters2004 import get_themesdvd
from magazines.igromania.includes.settings import MAGAZINE_NUMBER


def fill_magazine(request):
    """
    добавляет в базу существующие выпуски журнала

    :param request:
    """
    current_year = 1997
    current_month = 10

    for item in range(1, 223):
        models.Magazine(number=item, public_year=current_year, public_month=current_month).save()
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
            models.Game(title=item).save()
        except IntegrityError, e:
            print('%s уже есть, %s' % (item, e))


def fill_patches(request):
    """
    добавляет в базу инфу по патчам из выпуска

    :param request:
    """
    games = sorted(get_patches_2000()[0])
    patches = get_patches_2000()[1]

    games_qset = []
    for item in models.Game.objects.all():
        if item.title in games:
            games_qset.append(item)

    for i, item in enumerate(games):
        print(games_qset[i])

        models.Patch(magazine_id=28, game_id=int(games_qset[i].id), version=patches[i][1][1],
                     description=patches[i][3][1]).save()


def fill_demos(request):
    """
    добавляет в базу инфу по демоверсиям из выпуска

    :param request:
    """
    games = get_demos_2000()[0]
    demos = get_demos_2000()[1]

    games_qset = []
    for item in models.Game.objects.all():
        if item.title in games:
            games_qset.append(item)

    for i, item in enumerate(games):
        print(games_qset[i])

        models.Demo(magazine_id=28, game_id=games_qset[i].id, developer=demos[i][2][1], publisher=demos[i][3][1],
                    genre=demos[i][4][1], sysreq=demos[i][5][1], description=demos[i][6][1]).save()

    for entry in models.Demo.objects.order_by('-id')[:len(games)]:
        for item in games:
            if entry.game.title == item:
                for img in demos[games.index(item)][-2:]:
                    print('magazine/demo/%s' % img[1])
                    print(entry.id)
                    models.DemoImg(game_id=entry.id, image='magazine/demo/%s' % img[1]).save()


def fill_themesdvd():
    data = get_themesdvd()
    for item in data.values():
        print(item['Title'])
        models.ThemeDVD(magazine_id=MAGAZINE_NUMBER, title=item['Title'], description=item['Content']).save()
