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
# Print list of candidates
    candidate_count = {}
    candidate_count = csv.DictReader(data, "Candidate")

# Print percentage of votes per candidate
    print(candidate_count)

# Print total number of votes per candidate


# Produce output file
    