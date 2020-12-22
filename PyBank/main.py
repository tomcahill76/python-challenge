import os 
import csv

csvpath = os.path.joinC:(Users,Dell,Documents,waus-perth-data-pt-12-2020-u-c,'02-Homework','03-Python',Instructions,PyBank,Resources', 'budget_data.csv')
with open(csvpath) as csvfile
csvreader= csvreader(csvfile,demitire=',')
csv_header=next(csv_reader)
for row in csvreader:
    print row