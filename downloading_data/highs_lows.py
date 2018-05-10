import csv
import matplotlib.pyplot as plt
from datetime import datetime
# get dates, high and low temperature from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
# for index, column_header in enumerate(head_row):
 #   print(index,column_header)
# print(head_row)
# get dates and high temperatures from file
    highs, dates, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# print(highs)
# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# format plot
plt.title('Daily high tempretures -2014\n Death Valley,CA', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Tempreture (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
