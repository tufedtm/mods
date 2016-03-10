# coding=utf-8
from __future__ import unicode_literals
import os
import configparser
from pprint import pprint
from settings import MAGAZINE_FOLDER, MAGAZINE_NUMBER

############### почти рабочий вариант
# def dd(config, sections, name):
#     for section in sections:
#         if config.items(section)[0][1] == 'File':
#             if name in section:
#                 return dict(config.items(section))
#
#
# def get_gamezone():
#     gz1_config = configparser.ConfigParser(delimiters='=')
#     gz1_config.optionxform = str
#     gz1_config.read(MAGAZINE_FOLDER + 'gamezone1/data.ini')
#
#     # САМЫЙ НОРМАЛЬНЫЙ КУСОК
#     # data = {}
#     # for section in gz1_config.sections():
#     #     items = gz1_config.items(section)
#     #     tmp = {}
#     #     for item in items:
#     #         tmp[item[0]] = item[1]
#     #     data[section] = tmp
#     # pprint(data)
#
#
#
#     sections = gz1_config.sections()
#     data = {}
#
#     name = ''
#     current_section = ''
#     for section in sections:
#         items = gz1_config.items(section)
#
#         if items[0][1] == 'Menu':
#             name = items[1][1]
#             current_section = section
#             data[section] = {}
#             for item in items:
#                 data[section][item[0]] = item[1]
#             data[section]['childs'] = {}
#         elif items[0][1] == 'File':
#             data[current_section]['childs'][section] = dd(gz1_config, sections, name)
#             # for item in data:
#             #     if name in section:
#             #         print(item, name, current_section, section)
#         else:
#             continue
#
#
#             # data[section] = menu
#         # elif items[0][1] == 'Return':
#         #     print(section)
#         # elif items[0][1] == 'File':
#         #     tmp = {}
#         #     for item in items:
#         #         tmp[item[0]] = item[1]
#         #
#         #     data[section]['childs'].append(tmp)
#
#     pprint(data)

############### / почти рабочий вариант


# todo: список папок в номере с data.ini

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


get_ini_folders()


# todo: парсинг под каждую отдельно

def dd(config, sections, name):
    for section in sections:
        if config.items(section)[0][1] == 'File':
            if name in section:
                return dict(config.items(section))


def get_gamezone():
    gz1_config = configparser.ConfigParser(delimiters='=')
    gz1_config.optionxform = str
    gz1_config.read(MAGAZINE_FOLDER + 'gamezone1/data.ini')

    # САМЫЙ НОРМАЛЬНЫЙ КУСОК
    # data = {}
    # for section in gz1_config.sections():
    #     items = gz1_config.items(section)
    #     tmp = {}
    #     for item in items:
    #         tmp[item[0]] = item[1]
    #     data[section] = tmp
    # pprint(data)



    sections = gz1_config.sections()
    data = {}

    name = ''
    current_section = ''
    for section in sections:
        items = gz1_config.items(section)

        if items[0][1] == 'Menu':
            name = items[1][1]
            current_section = section
            data[section] = {}
            for item in items:
                data[section][item[0]] = item[1]
            data[section]['childs'] = {}
        elif items[0][1] == 'File':
            data[current_section]['childs'][section] = dd(gz1_config, sections, name)
            # for item in data:
            #     if name in section:
            #         print(item, name, current_section, section)
        elif items[0][1] == 'Return':
            next_section = sections[sections.index(section) + 1]
            if gz1_config.items(next_section)[0][1] == 'Menu':
                data[current_section]['childs'][section] = {}


            # data[section] = menu
        # elif items[0][1] == 'Return':
        #     print(section)
        # elif items[0][1] == 'File':
        #     tmp = {}
        #     for item in items:
        #         tmp[item[0]] = item[1]
        #
        #     data[section]['childs'].append(tmp)

    pprint(data)




    # pprint(data)

    # print(len(data))

    # data = {}
    # for section in gz1_config.sections():
    #     tmp_data = {}
    #     for value in range(len(gz1_config.items(section))):
    #         if gz1_config.items(section)[value][1] == 'Menu':
    #             print(section)
    #         tmp_data[gz1_config.items(section)[value][0]] = gz1_config.items(section)[value][1]
    #     data[section] = tmp_data
    #
    # pprint(data)

    # data1 = data
    # for key in data:
    #     print(key)
    #     for value in range(len(data[key])):
    #         print(data[key][value])
    #         print(data[key][value][0])
    #         print(data[key][value][1])
    #         data1[key][data[key][value][0]] = data[key][value][1]
        #
        # pprint(len(data[item]))


    # first_section = gz1_config.sections()[0]
    # name = dict(gz1_config.items(first_section))['Name']
    # count = int(dict(gz1_config.items(first_section))['All'])
    #
    # top_menu_sections = []
    # for i in range(1, count + 1):
    #     top_menu_sections.append('%s_%s%d' % (first_section, name, i))
    # print(top_menu_sections)


    #     print(name, section)
    #     print(gz1_config.sections())
        # print(gz1_config.options())

        # 'AZONE_' + name + unicode(section)

    # print(dict(gz1_config.items()))

    # sections = gz1_config.sections()
    # tmp_sections = []
    # for section in sections:
    #     item = dict(gz1_config.items(section))
    #
    #     if 'Title' in item.keys() and item['Type'] == 'Menu':
    #         tmp_sections.append(section)
    #
    # print(tmp_sections)
    #
    # for section in tmp_sections:
    #     item = dict(gz1_config.items(section))
    #     print(item['Name'])
    #     print(section)
    #     if item['Name'] in section:
    #         print(section)


get_gamezone()
