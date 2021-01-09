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
    Greatest_Increase = 0
    Greatest_Decrease = 0 
    

    for row in csvreader:
        TotalNet += float(row[1])
        loop_count += 1
        avg_net = int(TotalNet/loop_count)
        # print(row[1])
        # print(type(row[1]))
        Change = int(row[1]) - int(lastnet)
        ChangeTotal += int(Change)
        avg_change = ChangeTotal / loop_count
        lastnet = int(row[1])
        if int(Change) >= int(Greatest_Increase):
            Greatest_Increase = Change
            Greatest_Increase_mth = row[0]
        if int(Change) <= int(Greatest_Decrease):
            Greatest_Decrease = Change
            Greatest_Decrease_mth = row[0]

    
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {loop_count}')
    print("Total: ${:,.0f}".format(TotalNet))
    print("Average  Change:  ${:,.0f}".format  (avg_change))
    print("Greatest Increase in Profits: " + Greatest_Increase_mth + " ${:,.0f} ".format(Greatest_Increase))
    print("Greatest Decrease in Profits: " + Greatest_Decrease_mth + " ${:,.0f} ".format(Greatest_Decrease))

    # Write file to
    report_path = os.path.join("Analysis", "Financial_Analysis.txt")

    # Open the file in "write" mode. Specify the variables
    with open(report_path, 'w') as report:
        report.write("Financial Analysis\n")
        report.write("----------------------------\n")
        report.write(f'Total Months: {loop_count}\n')
        report.write("Total: ${:,.0f}\n".format(TotalNet))
        report.write("Average  Change:  ${:,.0f}\n".format  (avg_change))
        report.write("Greatest Increase in Profits: " + Greatest_Increase_mth + " ${:,.0f} \n".format(Greatest_Increase))
        report.write("Greatest Decrease in Profits: " + Greatest_Decrease_mth + " ${:,.0f} \n".format(Greatest_Decrease))

    
    
    