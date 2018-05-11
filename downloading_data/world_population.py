from country_codes import get_country_code
import json
import pygal
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
wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_population)
wm.render_to_file('world_population.svg')
