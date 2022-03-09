import csv

csvpath = "Resources/election_data.csv"

#Initialize Variables
total_votes = 0

#Create the set lists to store data
candidates = set()

# Names gained from Unique List of Canidates
candidates_dict = {
    "Li": 0,
    "O'Tooley": 0,
    "Khan": 0,
    "Correy": 0
}

with open(csvpath, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)

    for row in csvreader:
    
        # Total Votes
        total_votes += 1

        # UNIQUE LIST OF CANDIDATES
        candidates.add(row[2])

        #add to the vote count of the canidate if the vote was for the canidate in the canidate column
        if row[2] == "Li":
            candidates_dict["Li"] += 1
        elif row[2] == "Khan":
            candidates_dict["Khan"] += 1
        elif row[2] == "O'Tooley":
            candidates_dict["O'Tooley"] += 1
        else:
            candidates_dict["Correy"] += 1



print(total_votes)
print(candidates)
print(candidates_dict)

# Grab the the canidate with the most votes based on the canidate dictionary
max_cand = max(candidates_dict, key=candidates_dict.get)
max_votes = candidates_dict[max_cand]

results = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n"""
# Print results of the vote counts per canidate and calculate the percentage of the votes that each canidate got.
for canidate in candidates_dict.keys():
    perc = 100*(candidates_dict[canidate] / total_votes)
    results += f"{canidate}: {round(perc, 2)}% ({candidates_dict[canidate]})\n"


results += f"""-------------------------
Winner: {max_cand}
-------------------------
"""

print(results)

# writes to file
with open("analysis.txt", "w") as file:
    file.write(results)

