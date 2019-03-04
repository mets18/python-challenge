# import dependencies
import os
import csv

# convert csv
election = os.path.join ("resources","election_data.csv")
with open(election, 'r') as csvfile:
    data = csvfile
    csvreader = csv.reader(data, delimiter=',')

# The total number of votes included in the dataset
    row_count = sum(1 for row in csvreader)-1

# Print total votes
    print(row_count)
# Reset csvreader
    data.seek(0)
# Skip header row
    header = next(csvreader)

# Print list of candidates
    count = {}
    for candidate in csvreader:
        if candidate [2] not in count:
            count [candidate [2]] = 1
        else:
            count [candidate [2]] = count[candidate [2]] + 1
    print (count)


# Print percentage of votes per candidate
#print(len(candidate_count["Candidate"])

# Print total number of votes per candidate
