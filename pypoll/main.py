#ppoll challenge
#import data

# A Note To The T/A Grading This:
# I did not spend my time on this one. 
# There's no way it works. But the psuedo code is there. ..kind of 

import os
import csv

OfficialCount = os.path.join("election-data.csv")


# Open & read the file, skip the header
with open(OfficialCount, newline="") as votes_csv:
    csvreader = csv.reader(votes_csv, delimiter=",")
    csv_header = next(votes_csv)

    #set up a library of candidates
    Candidates = ("Khan","Correy","Li","O'Tooley")

    #and variables for counting, totaling votes
    Khan_votes = 0
    Correy_votes = 0
    Li_votes =0
    OTooley_votes =0


    #count total votes
    for row in Votes_csv
        Overall = row+1[2]+row[2]

    #count candidate votes
    for candidates in csvreader:
        if row[2]=="Khan":
            Khan_votes=Khan_votes +1
            elif row[2]=="Correy":
                Correy_votes = Correy_votes +1
            elif row[2]=="Li"
                Li_votes = Li_votes+1
            elif row[2]=="O'Tooley"
                OTooley_votes = OTooley_votes +1

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