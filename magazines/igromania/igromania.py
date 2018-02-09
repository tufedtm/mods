import os
import shutil

from .includes.getters import get_magazines
from .includes.getters2004 import get_gamezone, get_themesdvd, get_deathzone, get_demosthemes1, get_demosthemes2, \
    get_interest, get_patches
from .includes.settings import FOLDER_DEST, MAGAZINE_FOLDER

WARNING = '\033[93m'
ENDC = '\033[0m'


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


def copy_gamezone():
    data = get_gamezone()

    for item in data.values():
        print(item['Title'])
        for child in item['childs'].values():
            path = '%s/%s' % (child['Path'].split('\\')[0], child['Path'].split('\\')[1])
            src = '%s%s' % (MAGAZINE_FOLDER, path)
            print(src)
            dst = '%sgamezone/%s/%s' % (
                FOLDER_DEST, MAGAZINE_FOLDER.split('/')[3], item['Title'].replace(':', '-').replace('"', '')
            )
            print(dst)
            shutil.copytree(src, dst)
            break

    for i in range(1, 4):
        ini = MAGAZINE_FOLDER + 'GameZone' + str(i) + '/data.ini'
        dest = FOLDER_DEST + 'gamezone/' + MAGAZINE_FOLDER.split('/')[3] + '/'
        print(ini)
        print(dest)
        shutil.copy(ini, dest)
        os.rename(dest + 'data.ini', dest + 'data' + str(i) + '.ini')


def copy_themesdvd():
    data = get_themesdvd()

    for item in data.values():
        print(item['Title'])
        path = '%s/%s' % (item['Path'].split('\\')[0], item['Path'].split('\\')[1])
        src = '%s%s' % (MAGAZINE_FOLDER, path)
        print(src)
        dst = '%sthemesdvd/%s/%s' % (
            FOLDER_DEST, MAGAZINE_FOLDER.split('/')[3], item['Title'].replace(':', '-').replace('"', '')
        )
        print(dst)
        shutil.copytree(src, dst)

    ini = MAGAZINE_FOLDER + 'ThemesDVD/data.ini'
    dest = FOLDER_DEST + 'themesdvd/' + MAGAZINE_FOLDER.split('/')[3]
    shutil.copy(ini, dest)


def copy_deathzone():
    data = get_deathzone()

    for item in data.values():
        print(item['Title'])
        for child in item['childs'].values():
            path = '%s/%s' % (child['Path'].split('\\')[0], child['Path'].split('\\')[1])
            src = '%s%s' % (MAGAZINE_FOLDER, path)
            print(src)
            dst = '%sdeathzone/%s/%s' % (
                FOLDER_DEST, MAGAZINE_FOLDER.split('/')[3], item['Title'].replace(':', '-').replace('"', '')
            )
            print(dst)
            shutil.copytree(src, dst)
            break

    ini = MAGAZINE_FOLDER + 'DeathZone/data.ini'
    dest = FOLDER_DEST + 'deathzone/' + MAGAZINE_FOLDER.split('/')[3]
    shutil.copy(ini, dest)


def copy_demosthemes1():
    data = get_demosthemes1()

    for item in data.values():
        print(item['Title'])
        if item.get('Path'):
            path = '%s/%s' % (item.get('Path').split('\\')[0], item.get('Path').split('\\')[1])
        elif item.get('Name'):
            path = '%s/%s' % (item.get('Name').split('\\')[0], item.get('Name').split('\\')[1])
        else:
            print(WARNING + 'файла на диске нет' + ENDC)
            continue

        src = '%s%s' % (MAGAZINE_FOLDER, path)
        print(src)
        dst = '%sdemosthemes1/%s/%s' % (
            FOLDER_DEST, MAGAZINE_FOLDER.split('/')[3], item['Title'].replace(':', '-').replace('"', '')
        )
        print(dst)
        shutil.copytree(src, dst)

    ini = MAGAZINE_FOLDER + 'DemosThemes1/data.ini'
    dest = FOLDER_DEST + 'demosthemes1/' + MAGAZINE_FOLDER.split('/')[3]
    shutil.copy(ini, dest)


def copy_demosthemes2():
    data = get_demosthemes2()

    for item in data.values():
        print(item['Title'])
        if item.get('Path'):
            path = '%s/%s' % (item.get('Path').split('\\')[0], item.get('Path').split('\\')[1])
        elif item.get('Name'):
            path = '%s/%s' % (item.get('Name').split('\\')[0], item.get('Name').split('\\')[1])
        else:
            print(WARNING + 'файла на диске нет' + ENDC)
            continue

        src = '%s%s' % (MAGAZINE_FOLDER, path)
        print(src)
        dst = '%sdemosthemes2/%s/%s' % (
            FOLDER_DEST, MAGAZINE_FOLDER.split('/')[3], item['Title'].replace(':', '-').replace('"', '')
        )
        print(dst)
        shutil.copytree(src, dst)

    ini = MAGAZINE_FOLDER + 'DemosThemes2/data.ini'
    dest = FOLDER_DEST + 'demosthemes2/' + MAGAZINE_FOLDER.split('/')[3]
    shutil.copy(ini, dest)


def copy_interest():
    data = get_interest()

    for item in data.values():
        print(item['Title'])
        if item.get('Path'):
            path = '%s/%s' % (item.get('Path').split('\\')[0], item.get('Path').split('\\')[1])
        elif item.get('Name'):
            path = '%s/%s' % (item.get('Name').split('\\')[0], item.get('Name').split('\\')[1])
        else:
            print(WARNING + 'файла на диске нет' + ENDC)
            continue

        src = '%s%s' % (MAGAZINE_FOLDER, path)
        print(src)
        dst = '%sinterest/%s/%s' % (
            FOLDER_DEST, MAGAZINE_FOLDER.split('/')[3], item['Title'].replace(':', '-').replace('"', '')
        )
        print(dst)
        shutil.copytree(src, dst)

    ini = MAGAZINE_FOLDER + 'Interest/data.ini'
    dest = FOLDER_DEST + 'interest/' + MAGAZINE_FOLDER.split('/')[3]
    shutil.copy(ini, dest)


def copy_patches():
    data = get_patches()

    for item in data.values():
        print(item['Title'])
        if item.get('Path'):
            path = '%s/%s' % (item.get('Path').split('\\')[0], item.get('Path').split('\\')[1])
        elif item.get('Name'):
            path = '%s/%s' % (item.get('Name').split('\\')[0], item.get('Name').split('\\')[1])
        else:
            print(WARNING + 'файла на диске нет' + ENDC)
            continue

        src = '%s%s' % (MAGAZINE_FOLDER, path)
        print(src)
        dst = '%spatches/%s/%s' % (
            FOLDER_DEST, MAGAZINE_FOLDER.split('/')[3], item['Title'].replace(':', '-').replace('"', '')
        )
        print(dst)
        shutil.copytree(src, dst)

    ini = MAGAZINE_FOLDER + 'Patches/data.ini'
    dest = FOLDER_DEST + 'patches/' + MAGAZINE_FOLDER.split('/')[3]
    shutil.copy(ini, dest)
