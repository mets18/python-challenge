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

# Reset csvreader
    data.seek(0)
# Print total votes
    print(row_count)
    data.seek(0)

    