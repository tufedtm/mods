import os

os.system('cls')

dirPath = 'e:/~~/disciples/disciples/disciples 3/mods/'
icon = 'd:/tools/max payne/icon.png'
img = 'd:/tools/max payne/img.bmp'

# print(os.listdir(dirPath))
# print(dirPath + os.listdir(dirPath)[0])


for i in os.listdir(dirPath):
    os.system('7z a -sfx7z.sfx "' + dirPath + i + ' 7z.exe" "' + dirPath + i + '/*" -mx=9 -mmt=16 -ms=off')
    os.system('rar a -sfx -md1g -m5 "' + dirPath + i + ' winrar.exe" "' + dirPath + i + '/*" -ep1 -mt16 -r -s-')

# -iiconc:\myicons\ver1.ico
# -iimglogo2.bmp
#  -iicon' + icon + '
# -iimg' + img
