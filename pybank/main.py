#bank challenge
#import data
#git has got to get easier over time

import os
import csv

OfficialCount = os.path.join("budget_data.csv")


# Open & read the file, skip the header
with open("budget_data.csv", newline="") as budget_csv:
    csvreader = csv.reader("budget_csv", delimiter=",")
    csv_header = next(csvreader)

#calc total sales
for row in csvreader
    total_sales=sum.row[2]

#calc average sales
months = len(csvreader)
avg_sales = sum.row[2]/months

#calc changes
prev_value = 0
big_gain = 0
big_loss = 0

for row in csvreader:
    change = (row[1] - prev_value)
    prev_value = row[1]
if change > big_gain:
    big_gain = change
    gain_month = row[0]
    elif change < big_loss
        big_loss = change
        loss_month = row[0]
        else


# # #print all results in terminal
# print("Financial Analysis")
# print("---------------------------------------")
# print(f("Number of Months in Analysis: " months
#print(f("Total: ") + total_sales)
# print(f("Average Change: ") avg_sales)
# print(f"Greatest Increase in Profits: ") gain_month + "(" + big_gain + ")")
# print(f"Greatest Decrease in Profits: ") loss_month + "(" + big_loss + ")")

# export a text file with the results
# save the output file path


# open the output file, create a header row, and then write the zipped object to the csv
# output = os.path.join("output.csv")
# with open(output, "w", newline="") as financial_analysis:
#     writer = csv.writer(financial_analysis)

#     writer.writerow([ *this line is questionable. i don't have indexes to declare. but i prob need to have /
# something here? or maybe since i don't have indexes (b/c this is one file, not a bunch of lists I don't have to have
# this line and i can just skip to the next part, "writer.writerows(financial_analysis")])

#     writer.writerows(financial_analysis)


