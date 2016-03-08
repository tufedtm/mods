# coding=utf-8
from __future__ import unicode_literals
import configparser
import os
import shutil
from includes.getters import get_magazines, get_data_sections_2000
from includes.settings import FOLDER_DEST, MAGAZINE


def patches_2000():
    """
    возвращает информацию по патчам с выпуска журнала

    :return: список списков кортежей
    """
    sections = get_data_sections_2000()
    config = configparser.ConfigParser(delimiters='=')
    config.optionxform = str
    config.read('%sdata/data.txt' % MAGAZINE)

    sections = [x for x in sections if 'patches' in x.lower()]

    games = []

    for section in sections:
        if config.has_section(section):
            games.extend(config.options(section))

    games = [x for x in games]

    res = []
    for section in games:
        if section in config.sections():
            res.append(config.items(section))

    return res


def xa(src_path):
    """
    переносит всю музыку с диска в подпапку FOLDER_DEST
    вызываем так
    xa('e:/~/игромания 2000/')
    содержимое e:/~/игромания 2000/
        игромания 2000.28.01
        игромания 2000.29.02
        ...

    :param src_path: путь к папке с распаковынными дисками
    """
    folders = get_magazines(src_path)
    magazine_numbers = [x for x in folders]

    for folder in folders:
        folder_src = os.path.join(src_path, folder)

        for item in os.listdir(folder_src):
            if item.lower() == 'xa':
                src = '%s/%s' % (folder_src, item)
                dst = '%sxa/%s' % (FOLDER_DEST, magazine_numbers[folders.index(folder)])
                shutil.copytree(src, dst)
