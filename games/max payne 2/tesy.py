import json
from pprint import pprint

ss = open('info.json')
ss = json.load(ss)

pprint(ss['mods'])
