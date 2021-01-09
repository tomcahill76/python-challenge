import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
#def goes here
    #date [0]
    #net [1]
    loop_count = 0
    total_net = 0

#variables goes here
    # loop_count
    # total_net tracker
#loop goes here
    # for x in ......
        # loop_count += 1
        # total_net += total_net + net
    # for row in csvreader:
    #     print(row)
    loop_count = 0
    net = int(csvfile[1])
    total_net = 0
    
        loop_count +=1
        print(loop_count)
        total_net = net + total_net
        print(total_net)
