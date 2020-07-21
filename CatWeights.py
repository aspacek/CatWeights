# Import plot routine:
import matplotlib.pyplot as plt
# Import routine to mimic 'sed' in python:
import fileinput
# Import routine to read/write csv files:
import csv

# Remove extra tab in the data to easily read it in with csv:
for line in fileinput.input('CatWeights.txt', inplace=True):
	print(line.replace('\t\t', '\t'), end='')

# Read in data
with open('CatWeights.txt') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')
	date = []
	location = []
	cat = []
	weight = []
	for row in csv_reader:
		if len(row) == 4:
			date = date+[row[0]]
			location = location+[row[1]]
			cat = cat+[row[2]]
			weight = weight+[row[3]]
date = [int(i) for i in date]
weight = [float(i) for i in weight]

# Put the tab back in the data file:
for line in fileinput.input('CatWeights.txt', inplace=True):
	print(line.replace('\t', '\t\t'), end='')

# Separate Sneezy and Flurry data:
Sdate = []
Slocation = []
Scat = []
Sweight = []
Fdate = []
Flocation = []
Fcat = []
Fweight = []
for i in range(len(date)):
	if cat[i] == 'Sneezy':
		Sdate = Sdate+[date[i]]
		Slocation = Slocation+[location[i]]
		Scat = Scat+[cat[i]]
		Sweight = Sweight+[weight[i]]
	elif cat[i] == 'Flurry':
		Fdate = Fdate+[date[i]]
		Flocation = Flocation+[location[i]]
		Fcat = Fcat+[cat[i]]
		Fweight = Fweight+[weight[i]]

# Make plot:
plt.plot(Sdate,Sweight,label='Sneezy')
plt.plot(Fdate,Fweight,label='Flurry')
plt.xlabel('Date (yr/mo/dy)')
plt.ylabel('Weight (lb)')
plt.legend(loc='upper right')
plt.savefig('CatWeights.png')
