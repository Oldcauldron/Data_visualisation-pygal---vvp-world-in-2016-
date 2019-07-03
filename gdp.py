
import json
import pygal
# from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle as RS

from get_code import bicode


# def bicode(name):
#     with open('add_correct_cods.json') as acc:
#                 correct = json.load(acc)
#     for a, b in COUNTRIES.items():
#         if b == name:
#             return a
#         elif name in correct:
#             return correct[name]
#     return None


wm_dic_1 = {}
wm_dic_2 = {}
wm_dic_3 = {}
with open('gdp_json.json') as f:
    gdp_file = json.load(f)
for i in gdp_file:
    if i['Year'] == 2016:
        country = i['Country Name']
        value = int(float(i['Value'])) / 1000000
        code = bicode(country)
        if value < 1000000:
            wm_dic_1[code] = value
        elif value < 10000000:
            wm_dic_2[code] = value
        else:
            wm_dic_3[code] = value


wm_style = RS('#990000')
wm = pygal.maps.world.World(style=wm_style)

wm.title = 'vvp world in 2016'

wm.add('> 10000 mlrd', wm_dic_3)
wm.add('1000 mlrd - 10000 mlrd', wm_dic_2)
wm.add('< 1000 mlrd', wm_dic_1)

wm.render_to_file('vvp_world_2016.svg')


