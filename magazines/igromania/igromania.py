# coding=utf-8
from __future__ import unicode_literals

import os
import shutil
from includes.getters import get_magazines
from includes.settings import FOLDER_DEST


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
            if item in ['xa', 'Xa', 'XA']:
                src = '%s/%s' % (folder_src, item)
                dst = '%sxa/%s' % (FOLDER_DEST, magazine_numbers[folders.index(folder)])
                shutil.move(src, dst)

