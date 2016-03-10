# coding=utf-8
from __future__ import unicode_literals
import os
import configparser
from settings import MAGAZINE_FOLDER, MAGAZINE_NUMBER


def get_ini_2000():
    """
    возвращает содержимое файла с данными

    :return: объект configparser
    """
    config = configparser.ConfigParser(delimiters='=')
    config.optionxform = str
    config.read('%sdata/data.txt' % MAGAZINE_FOLDER)

    return config


def get_magazines(src_path):
    """
    возвращает все журналы за год

    :param src_path: путь к папке с папками 12 журналов за год
    :return: изменяемый список с названиями папок
    """
    # todo: удалить функцию, т.к. правильнее копировать все файлы из одного журнала, а не одну папку со всех журналов
    return os.listdir(src_path)


def get_data_sections_2000():
    """
    возвращает все секции за месяц

    :return: изменяемый список с названиями секций
    """
    config = get_ini_2000()

    sections = []
    for section in config.sections():
        if not config.has_option(section, 'Install'):
            sections.append(section)

    return sections


def get_games_2000_all():
    """
    возвращает список игр в выпуске

    :return: список строк с названиями игр
    """
    config = get_ini_2000()

    notgame_sections = []
    if MAGAZINE_NUMBER in [28]:
        notgame_sections = ['PROGRAM', 'SOFT', 'UTILS']
    elif MAGAZINE_NUMBER in [29, 30]:
        notgame_sections = ['PROGRAM', 'RUSSIA', 'BUNKER', 'SOFT', 'UTILS']

    games = []
    for section in get_data_sections_2000():
        if section not in notgame_sections:
            games.extend(config.options(section))

    return sorted(games)


print(get_games_2000_all())

def get_games_2000_section(sections):
    """
    возвращает список игр в переданной секции

    :param sections: список названий секций
    :return: список названий игр
    """
    config = get_ini_2000()

    games = []
    for section in sections:
        if config.has_section(section):
            games.extend(config.options(section))

    return games


def get_patches_2000():
    """
    возвращает информацию по патчам с выпуска журнала

    :return: список секций в патчах
    :return: список списков кортежей
    """
    config = get_ini_2000()

    sections = get_data_sections_2000()
    sections = [x for x in sections if 'patches' in x.lower()]

    games = get_games_2000_section(sections)

    res = []
    for section in games:
        if section in config.sections():
            res.append(config.items(section))

    return games, res


def get_demos_2000():
    """
    возвращает информацию по демоверсиям с выпуска журнала

    :return: список секций в демоверсиях
    :return: список списков кортежей
    """
    config = get_ini_2000()
    sections = get_data_sections_2000()
    sections = [x for x in sections if 'demo' in x.lower()]

    games = get_games_2000_section(sections)

    demos = []
    for section in games:
        if section in config.sections():
            demos.append(config.items(section))

    return sorted(games), sorted(demos)
