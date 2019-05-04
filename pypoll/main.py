#ppoll challenge
#import data

import os
import csv

OfficialCount = os.path.join(".." "desktop" "python-challenge","pypoll","election-data.csv")


# Open & read the file, skip the header
with open(OfficialCount, newline="") as votes_csv:
    csvreader = csv.reader(votes_csv, delimiter=",")
    csv_header = next(votes_csv)

    #set up a library of candidates
    Candidates = ("Khan","Correy","Li","O'Tooley")

    #count total votes
    for row in Votes_csv
        Overall = row+1[2]+row[2]

    #count candidate votes
    for candidates in Votes_csv:
        votes_rec = row[2]+row+1[2]

    #calc percentage of votes
    for candidates in Votes_csv:
        Percentage = votes_rec/Overall

    #determine a winner
    for candidates in Votes_csv:
        if candidate percentage ....
        winner winner chicken dinner

    #print results
    print("Election Results")
    print("-----------------")
    print("Total Votes" + int(Overall))
    print("-----------------")
    print(Candidates,": " + Percentage +("%") + "(" + Overall + ")
    print("-----------------")
    print("Winner: " + winner)

    # # save the output file path
# output_file = os.path.join("output.csv")

# # open the output file, create a header row, and then write the zipped object to the csv
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     writer.writerow(["Index", "Employee", "Department"])

#     writer.writerows(roster)