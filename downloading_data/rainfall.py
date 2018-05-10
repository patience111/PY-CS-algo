import csv
from datetime import datetime
import matplotlib.pyplot as plt
dates, rainfalls = [], []
with open('sitka_rainfall_2015.csv') as f:
    reader = csv.reader(f)
    reader_head = next(reader)
# for number, value in enumerate(reader_head):
#   print(number,value)
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            rainfall = float(row[19])
        except:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)
            # compute cumulative
# plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfalls, c='blue', alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)
# format plot
title = 'Daily rainfall amounts - 2015\n Sitka, AK'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall(in)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
