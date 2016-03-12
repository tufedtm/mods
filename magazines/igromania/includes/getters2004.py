# coding=utf-8
from __future__ import unicode_literals
import os
import configparser
from pprint import pprint
from settings import MAGAZINE_FOLDER, MAGAZINE_NUMBER


def get_ini_folders():
    """
    список папок в номере с data.ini

    :return: список
    """
    folders = []
    for item in [x for x in os.listdir(MAGAZINE_FOLDER)]:
        if os.path.isfile(os.path.join(MAGAZINE_FOLDER, item, 'data.ini')):
            folders.append(item)

    return sorted(folders)


# todo: парсинг под каждую отдельно

def ini_to_dict(path):
    """
    преобразует ini-файл в словарь

    :param path: путь к ini-файлу, либо к списку ini-файлов
    :return: словарь с элеметами `Menu` и словарь с элементами `File`
    """
    config = configparser.RawConfigParser(delimiters='=')
    config.optionxform = str
    config.read(path)

    sections = config.sections()
    tmp = {}
    data = {}
    data_file = {}

    for section in sections:
        items = config.items(section)

        if items[0][1] == 'Menu':
            for item in items:
                tmp[item[0]] = item[1]
            data[section] = tmp
            data[section]['childs'] = {}
            tmp = {}
        elif items[0][1] == 'File':
            for item in items:
                tmp[item[0]] = item[1]
            data_file[section] = tmp
            tmp = {}
        else:
            tmp = {}

    return data, data_file


def get_gamezone():
    """
    создает словарь со всей gamezone выпуска

    :return: словарь
    """
    data, data_file = ini_to_dict([MAGAZINE_FOLDER + 'gamezone1/data.ini', MAGAZINE_FOLDER + 'gamezone2/data.ini',
                                   MAGAZINE_FOLDER + 'gamezone3/data.ini'])

    for key in data.keys():
        if key in ['AZONE', 'BZONE', 'CZONE']:
            data.pop(key)
        elif len(key.split('_')) > 2:
            data.pop(key)
        # закомментировать след. две строки для номера 85 (2004.10 окбябрь)
        elif 'AZO1' == key.split('_')[1]:
            data.pop(key)

    for key in data_file.keys():
        if 'OBSchA' in key:
            data_file.pop(key)
        elif key.split('_')[2] in ['Raboti2', 'Raboti3']:
            data_file.pop(key)

    for key in data_file.keys():
        for menu_key in data.keys():
            if key.split('_')[1] == menu_key.split('_')[1]:
                data[menu_key]['childs'][key] = data_file.get(key)

    return data


def get_themesdvd():
    """
    создает словарь со всей themedvd выпуска

    :return: словарь
    """
    data, data_file = ini_to_dict(MAGAZINE_FOLDER + 'ThemesDVD/data.ini')

    return data_file


def get_deathzone():
    """
    создает словарь со всей deathzone выпуска

    :return: словарь
    """
    data, data_file = ini_to_dict(MAGAZINE_FOLDER + 'DeathZone/data.ini')

    for key in data.keys():
        if key in ['Deathzone']:
            data.pop(key)
        elif len(key.split('_')) > 2:
            data.pop(key)

    # удаление руководства по установке
    data.pop('Deathzone_Dea%d' % len(data.keys()))

    for key in data_file.keys():
        for menu_key in data.keys():
            if key.split('_')[1] == menu_key.split('_')[1]:
                data[menu_key]['childs'][key] = data_file.get(key)

    return data


def get_interest():
    """
    создает словарь со всей interest выпуска

    :return: словарь
    """
    data, data_file = ini_to_dict(MAGAZINE_FOLDER + 'Interest/data.ini')

    return data_file


def get_demosthemes1():
    """
    создает словарь со всей demosthemes1 выпуска

    :return: словарь
    """
    data, data_file = ini_to_dict(MAGAZINE_FOLDER + 'DemosThemes1/data.ini')

    return data_file


def get_demosthemes2():
    """
    создает словарь со всей demosthemes2 выпуска

    :return: словарь
    """
    data, data_file = ini_to_dict(MAGAZINE_FOLDER + 'DemosThemes2/data.ini')

    return data_file


def get_patches():
    """
    создает словарь со всей patches выпуска

    :return: словарь
    """
    data, data_file = ini_to_dict(MAGAZINE_FOLDER + 'Patches/data.ini')

    return data_file
