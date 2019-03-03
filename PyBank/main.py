# import dependencies
import os
import csv

# convert csv
budgetcsv = os.path.join ("resources","budget_data.csv")

# Read in file and split the data
with open(budgetcsv, 'r') as csvfile:
    data = csvfile
    csvreader = csv.reader(data, delimiter=',')

# The total number of months included in the dataset
    row_count = sum(1 for row in csvreader)-1

# Reset csvreader
    data.seek(0)
# Skip header row    
    budget_header = next(csvreader)
# The net total amount of "Profit/Losses" over the entire period
    total=0
    for row in csvreader:
        total += float(row[1])
    
    

# The average of the changes in "Profit/Losses" over the entire period

    data.seek(0)
    budget_header = next(csvreader)
    original_value = next(csvreader)
    print (original_value[1])
    cells=list(csv.reader(data))
    last_value=(cells[(row_count)-2][1])
    print(last_value)
    average_change = (int(original_value[1]) - int(last_value))/(row_count-1)
    print("The average change is " + str(average_change) + ".")

# The greatest increase in profits (date and amount) over the entire period
      


# The greatest decrease in losses (date and amount) over the entire period

# Print results
    print("The number of rows is " + str(row_count) + ".")
    print ("The total profit/loss is $" + str(total) + ".")


# Produce output file
with open("output.txt", "w") as file:
    file.write("The number of rows is " + str(row_count) + ".\n")
    file.write("The total profit/loss is $" + str(total) + ".\n")
    file.write("The average change is " + str(average_change) + ".")
