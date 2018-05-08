import pygal
from die import Die
# create D6
die = Die()
# make same rolls,and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
# analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# print(len(frequencies))
# visulize the results
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.xtitle = 'Results'
hist.ytitle = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
