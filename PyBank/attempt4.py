import os
import csv

  
csvpath = os.path.join('Resources','budget_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
  
    header = next(csvreader)
    
    TotalNet = 0
    loop_count = 0
    Change = 0
    ChangeTotal = 0
    lastnet = 0
    

    for row in csvreader:
        net = int(row(1))
        TotalNet += float(net)
        loop_count += 1
        avg_net = int(TotalNet/loop_count)
        # Change = int(row(1) - lastnet)
        # ChangeTotal += int(Change)
        # avg_change = int(ChangeTotal / loop_count)
        # lastnet = int(row(1))


    print(str(TotalNet))
    print(loop_count)
    print(avg_net)
    #print(avg_change)
    