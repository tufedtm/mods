# coding=utf-8
from __future__ import unicode_literals
import os
import configparser
from settings import MAGAZINE


def get_magazines(src_path):
    """
    возвращает все журналы за год

    :param src_path: путь к папке с папками 12 журналов за год
    :return: изменяемый список с названиями папок
    """
    return os.listdir(src_path)


def get_data_sections_2000():
    """
    возвращает все секции за месяц

    :return: изменяемый список с названиями секций
    """
    config = configparser.ConfigParser(delimiters='=')
    config.read('%sdata/data.txt' % MAGAZINE)

    sections = []

    for section in config.sections():
        if not config.has_option(section, 'Install'):
            sections.append(section)

    return sections


def get_games_2000():
    """
    возвращает список игр в выпуске

    :return: список строк с названиями игр
    """
    config = configparser.ConfigParser(delimiters='=')
    config.optionxform = str
    config.read('%sdata/data.txt' % MAGAZINE)

    notgame_sections = ['PROGRAM', 'SOFT', 'UTILS']

    games = []
    for section in get_data_sections_2000():
        if section not in notgame_sections:
            games.extend(config.options(section))

    return games


def get_patches_2000():
    """
    возвращает информацию по патчам с выпуска журнала

    :return: список секций в патчах
    :return: список списков кортежей
    """
    config = configparser.ConfigParser(delimiters='=')
    config.optionxform = str
    config.read('%sdata/data.txt' % MAGAZINE)

    sections = get_data_sections_2000()
    sections = [x for x in sections if 'patches' in x.lower()]

    games = []
    for section in sections:
        if config.has_section(section):
            games.extend(config.options(section))

    res = []
    for section in games:
        if section in config.sections():
            res.append(config.items(section))

    return res, games
