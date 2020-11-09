#import necessary libraries
import os
import csv

# variables
month_count = 0
netTotalAmt = 0
prevAmt = 0  #need to calculate the changePL
changePL = 0  # calculated field for change from previous to this month
totalChangePL = 0 # each changePL totaled
avgTotalChange = 0
gIncProfitDate = ""
gIncProfitAmt = 0
gDecProfitDate = ""
gDecProfitAmt = 0
text_lines = []   # holds the analysis text
file_header = ""


# open the budget_data.csv file
rawdata_path = os.path.join(".", 'Resources', 'budget_data.csv')

with open(rawdata_path, encoding="utf8") as rawdata_file:

    # CSV reader specifies delimiter and variable that holds contents
    rawdata_reader = csv.reader(rawdata_file, delimiter=',')

    # store the header -- we don't use it anywhere though
    file_header = rawdata_reader
    
    # Read each row of data after the header
    next(rawdata_reader, None)
    for row in rawdata_reader:
        # update month count
        month_count = month_count + 1
        
        # update net total amount of P/L
        netTotalAmt = netTotalAmt + int(row[1])
        
        # get the change in P/L from last month    
        if prevAmt != 0:
            changePL = int(row[1]) - prevAmt
            # add to total change to calculate average later
            totalChangePL = totalChangePL + changePL
 
        # test for greatest profit and greatest loss
        if changePL > gIncProfitAmt:
            gIncProfitAmt = changePL
            gIncProfitDate = row[0]
        if changePL < gDecProfitAmt:
            gDecProfitAmt = changePL
            gDecProfitDate = row[0]
        # set prevAmt to current line to prepare for next row
        prevAmt = int(row[1])

# calculate the Average Change
totavgTotalChange = round(totalChangePL/month_count, 2)

# create text_lines
text_lines.append("Financial Analysis")
text_lines.append("---------------------------")
text_lines.append(f"Total Months: {month_count}")
text_lines.append(f"Total: ${netTotalAmt}")
text_lines.append(f"Average Change: ${totavgTotalChange}")
text_lines.append(f"Greatest Increase in Profits: {gIncProfitDate} (${gIncProfitAmt})")
text_lines.append(f"Greatest Decrease in Profits: {gDecProfitDate} (${gDecProfitAmt})")

# Save the report as analysis.txt
analysis_path = os.path.join(".", "analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(analysis_path, 'w', newline='') as analysis_file:
 
    for row in text_lines:
        analysis_file.write(row + "\n")
        print(row)






        


