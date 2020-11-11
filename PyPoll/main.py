# Calculate voter totals per candidate, and post winner
# PyPoll

import os
import csv
import decimal 

# Pseudo code
#  1. Read rows of input file, pull candidate and number of votes.
#  2. Using a dictionary, each Candidate and vote totals
#  3. Save and print to console.
 
# Declare and initialize variables
vote_d = {}
total_vote = 0
text_lines = []

# declare the decimal places as 3
decimal.getcontext = 5

# open input file election_data.csv
rawdata_path = os.path.join(".", 'Resources', 'election_data.csv')

with open(rawdata_path, encoding="utf8") as rawdata_file:

    # CSV reader specifies delimiter and variable that holds contents
    rawdata_reader = csv.reader(rawdata_file, delimiter=',')

    # Read each row of data after the header
    next(rawdata_reader, None)
    for row in rawdata_reader:
        total_vote += 1       
        # get candidate name and check if it's in the candidate_list.  
        if row[2] in vote_d:
            
            vote_d[f"{row[2]}"] = int(vote_d[f"{row[2]}"]) + 1
            
        # not in vote_d, so add the whole new key-value pair starting vote at 1
        else:
            vote_d[f"{row[2]}"] = 1

# calculate the winner
highest = ""
high_vote = 0
for candidate in vote_d:
    if int(vote_d[candidate]) > high_vote:
        highest = candidate
        high_vote = vote_d[candidate]
# create text_lines
text_lines.append("Election Results")
text_lines.append("-----------------------")
text_lines.append(f"Total Votes: {total_vote}")
text_lines.append("-----------------------")
for candidate in vote_d:
    # "{:.3%}.format(percentage_votes)
    percentage_votes = "{:.3%}".format(vote_d[candidate]/total_vote)
    text_lines.append(f"{candidate}: {percentage_votes} ({vote_d[candidate]})")
text_lines.append("-----------------------")
text_lines.append(f"Winner: {highest}")
text_lines.append("-----------------------")
# Save the report as analysis.txt
analysis_path = os.path.join(".", "analysis", "analysis.txt")


# Open the file using "write" mode. Specify the variable to hold the contents
with open(analysis_path, 'w', newline='') as analysis_file:
    # Initialize analysis.writer
    #analysis_writer = csv.writer(analysis_file, delimiter=',')
    
    for row in text_lines:
        analysis_file.write(row + "\n")
        print(row)