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
   
    print("-----------------------------------")
    print(f"Tolal votes {total_votes}")
    print("-----------------------------------")
    print(candidate)
    #print(k,  " : "+ (percentage)+ " : ",v)
    #print(f"percentate {percentage}")

    # Write file to
    report_path = os.path.join("Analysis", "Poll_Analysis.txt")

    # Open the file in "write" mode. Specify the variables
    with open(report_path, 'w') as report:
        report.write("----------------------------\n")
        report.write(f"Tolal votes {total_votes}\n")
        report.write("----------------------------\n")
        report.write(f"Summary: {candidate}\n")
        

    # print(candidate)
    # print(candidate.keys())
    
        # if statement 
            # if candidate <> last candidate and <> in candidate list then append candidate to candidate []
            # if candidate == any candidate then add count
            # make percentate



