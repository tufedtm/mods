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
        if config.has_option(section, 'Install'):
            break
        sections.append(section)

    return sections
