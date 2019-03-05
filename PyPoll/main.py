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
# Skip header row
    header = next(csvreader)

# Calculate election results
    count = {}
    for candidate in csvreader:
        if candidate [2] not in count:
            count [candidate [2]] = 1
        else:
            count [candidate [2]] = count[candidate [2]] + 1

    winner = [candidate for candidate in count.keys()][0]


# Print output
    print ("Election Results")
    print ("---------------------------------")
    print ("Total Votes: " + str(row_count))
    print ("---------------------------------")

    for candidate, value in count.items():
        print (candidate + ":  " + str(round(value / row_count * 100)) + "% " + "(" + str(value) + ")")

    print ("---------------------------------")
    print ("Winner: " + winner)
    print ("---------------------------------")

# Produce output file
with open("output.txt", "w") as file:
    file.write("Election Results\n")
    file.write("---------------------------------\n")
    file.write("Total Votes: " + str(row_count) + "\n")
    file.write("---------------------------------\n")
    for candidate, value in count.items():
        file.write (candidate + ":  " + str(round(value / row_count * 100)) + "% " + "(" + str(value) + ")\n")
    file.write("---------------------------------\n")
    file.write("Winner: " + winner + "\n")
    file.write("---------------------------------")
