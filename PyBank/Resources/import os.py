import os
import csv

csvpath = os.path.join('budget_data.csv')

with open (csvpath,'r') as csvfile:
    datareader = csv.reader(csvfile, delimiter = ',')

    # print(datareader)
    Header_Row = next(datareader)
    print(f"Header Row :{Header_Row}")