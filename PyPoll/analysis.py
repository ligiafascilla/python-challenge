# %%

import os
import csv

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
print(csvpath)

total_votes = 0
candidate_votes = {}
candidate_percentages = {}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
        else:
            candidate_votes[row[2]] = 1
    
    for candidate in candidate_votes:
        candidate_percentages[candidate] = "{:.3f}%".format(candidate_votes[candidate]/total_votes * 100)
    
    winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {candidate_percentages[candidate]} ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidate_votes:
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]} ({candidate_votes[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
