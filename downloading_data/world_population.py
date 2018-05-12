from country_codes import get_country_code
import json
import pygal
from pygal.style import RotateStyle as rs, LightColorizedStyle as lcs
# load the data into a list
with open('population_data.json') as f:
    pop_data = json.load(f)
# print the 2010 population for each country
# build dictionary of the pygal.map.world
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        #print(country_name + ":" + " " + str(population))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population
            #print(code + ':' + ' ' + str(population))
        # else:
            #print('ERROR - ' + country_name)
# group the countries into 3 population level
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# see how many countries are in each level
#print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
wm_style = rs('#336699', base_style=lcs)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
