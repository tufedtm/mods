import os

dirPath = 'd:/fc/fc1/mods'
icon = 'd:/tools/max payne/icon.png'
img = 'd:/tools/max payne/img.bmp'

for mod in os.listdir(dirPath):
    rar = f'rar a -ep1 -ma4 -m5 -md4m -qo- -r -se -sfx "{dirPath}/{mod} rar4" "{dirPath}/{mod}/*"'
    rar5 = f'rar a -ep1 -ma5 -htb -m5 -md1g -oi -qo- -r -se -sfx "{dirPath}/{mod} rar5" "{dirPath}/{mod}/*"'
    rar5oi1 = f'rar a -ep1 -ma5 -htb -m5 -md1g -oi:1 -qo- -r -se -sfx "{dirPath}/{mod} rar5 oi1" "{dirPath}/{mod}/*"'
    z7 = f''
    os.system(rar)
    os.system(rar5)
    os.system(rar5oi1)

# for i in os.listdir(dirPath):
#     print('7z a -sfx7z.sfx "' + dirPath + i + ' 7z.exe" "' + dirPath + i + '/*" -mx=9 -mmt=16 -ms=off')
