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

# open the budget_data.csv file
rawdata_path = os.path.join(".", 'Resources', 'budget_data.csv')
print(os.getcwd)
with open(rawdata_path, encoding="utf8") as rawdata_file:

    # CSV reader specifies delimiter and variable that holds contents
    rawdata_reader = csv.reader(rawdata_file, delimiter=',')

    # Read each row of data after the header
    for row in rawdata_reader:
        # update month count
        #need if statement to test what row we're on
        month_count = month_count + 1
        # update net total amount of P/L
        netTotalAmt = netTotalAmt + int(row[1])
        # test for greatest profit and greatest loss
        if int(row[1]) > gIncProfitAmt:
            gIncProfitAmt = int(row[1])
            gIncProfitDate = row[0]
        if int(row[1]) < gDecProfitAmt:
            gDecProfitAmt = int(row[1])
            gDecProfitDate = row[0]
        # get the change in P/L from last month    
        changePL = int(row[1]) - prevAmt
        # add to total change to calculate average later
        totalChangePL = totalChangePL + changePL

# calculate the Average Change
totavgTotalChange = totalChangePL/month_count

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
#    write("Financial Analysis\n")
#    write("---------------------------\n")
#    write(f"Total Months: {month_count}\n")
#    write(f"Total: ${netTotalAmt}\n)"
#    write(f"Average Change: ${totavgTotalChange}\n")
#    write(f"Greatest Increase in Profits: {gIncProfitDate} (${gIncProfitAmt})\n")
#    write(f"Greatest Decrease in Profits: {gDecProfitDate} (${gDecProfitAmt})\n")
    writelines(text_lines)

print(text_lines)





        


