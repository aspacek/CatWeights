###################
## CatWeights.py ##
###################

# sys module - reads in input values
#            - exits program on error
import sys

# pyplot module - plot out results
import matplotlib.pyplot as plt

# fileinput module - mimics 'sed' in python
import fileinput

# csv module - read and write csv files
import csv

##
## Written by Alex Spacek
## July 2020 - August 2020
##

# Read in inputs given in command:
#   >>python CatWeights.py input_file output_file cat_num name_1 name_2
#   inputs[0] = program filename
#   inputs[1] = input_file
#   inputs[2] = output_file
#   inputs[3] = cat_num
#   inputs[4] = name_1
#   inputs[5] = name_2
inputs = sys.argv
input_file = inputs[1]
output_file = inputs[2]
cat_num = int(inputs[3])

# Combine cat names:
names = []
for i in range(cat_num):
	names = names+[inputs[4+i]]

# Read in data
with open(input_file) as csv_file:
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

# Separate cat data:
for i in range(cat_num):
	Xdate = []
	Xlocation = []
	Xcat = []
	Xweight = []
	for j in range(len(date)):
		if cat[j] == names[i]:
			Xdate = Xdate+[date[j]]
			Xlocation = Xlocation+[location[j]]
			Xcat = Xcat+[cat[j]]
			Xweight = Xweight+[weight[j]]
	# Plot:
	plt.plot(Xdate,Xweight,label=names[i])

# Finish plot:
plt.xlabel('Date (yr/mo/dy)')
plt.ylabel('Weight (lb)')
plt.legend(loc='upper right')
plt.savefig(output_file)

