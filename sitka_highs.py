import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Visit NOAA Climate Date Online at https://www.ncdc.noaa.gov/cdo-web/
# In Discover Data by section, click Search Tool. In select a Dataset box,
# choose Daily Summaries

filename = 'data/West_Fayetteville_Weather_1951-2021.csv'
with open(filename) as f:
    # Return a reader object which will iterate over lines in the given csvfile
    reader = csv.reader(f)
    # Returns the next row of the reader’s iterable object as a list
    header_row = next(reader)

    # enumerate returns both index and value of each item in a list
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    # Get dates and high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot the high and low temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temps - 1951-2021 - West Fayetteville"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()