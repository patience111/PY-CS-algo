import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
# for index, column_header in enumerate(head_row):
 #   print(index,column_header)
# print(head_row)
# get dates and high temperatures from file
    highs, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
# print(highs)
# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
# format plot
plt.title('Daily high tempretures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Tempreture (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
