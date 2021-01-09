import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open (csvpath) as csv_election_file:
    csvreader = csv.reader(csv_election_file, delimiter = ',')
    #print(csvreader)

    #head row
    header = next(csvreader)
    #print(header)

    #Dim variables
    total_votes = 0
    candidate = {}
        

    for row in csvreader:
        if row[2] in candidate.keys():
            candidate[row[2]] += 1
        else:
            candidate[row[2]] = 1
        total_votes += 1

    for k, v  in candidate.items():
        percentage = int(v)/int(total_votes)
        #print((k) +" : " + (percentage) + " : " + (v) ) - I can't get this to work
        #Find winner
