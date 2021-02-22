import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    # Return a reader object which will iterate over lines in the given csvfile
    reader = csv.reader(f)
    # Returns the next row of the reader’s iterable object as a list
    header_row = next(reader)
    
    # enumerate returns both index and value of each item in a list
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    # Get high temps from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# plot the high temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot
plt.title("Daily high temps, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

print(highs)