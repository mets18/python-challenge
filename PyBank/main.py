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
 # Reset csvreader       
    data.seek(0)
# Skip header row and first row of data    
    budget_header = next(csvreader)
    original_value = next(csvreader)
# Calculate greatest increase and decrease
    previous_value = float(original_value[1])
    greatest_increase = 0
    greatest_decrease = 0
    for row in csvreader:
        current_change = float(row[1])-previous_value
        if current_change > greatest_increase:
            greatest_increase = current_change
            greatest_increase_month = row[0]
        else:
            greatest_increase = greatest_increase
        if current_change < greatest_decrease:
            greatest_decrease = current_change
            greatest_decrease_month = row[0]
        else:
            greatest_decrease = greatest_decrease
        

        previous_value = float(row[1])
       
    

# Reset csvreader
    data.seek(0)

# The average of the changes in "Profit/Losses" over the entire period
    cells=list(csv.reader(data))
    last_value=(cells[(row_count)][1])
    average_change = (int(last_value) - int(original_value[1]))/(row_count-1)
    



# Print results
    print ("Financial Analysis")
    print ("---------------------------------")
    print("Total months: " + str(row_count))
    print ("Total: $" + str(int(total)))
    print("Average change: " + str(int(average_change)))
    print ("Greatest Increase in Profits: " + (greatest_increase_month) + "  $" + str(int(greatest_increase)))
    print ("Greatest Decrease in Profits: " + (greatest_decrease_month) + "  $" + str(int(greatest_decrease)))

# Produce output file
with open("output.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------------\n")
    file.write("Total months: " + str(row_count) + "\n")
    file.write("Total: $" + str(int(total)) + "\n")
    file.write("Average change: " + str(int(average_change)) + "\n")
    file.write("Greatest Increase in Profits: " + (greatest_increase_month) + "  $" + str(int(greatest_increase)) + "\n")
    file.write("Greatest Decrease in Profits: " + (greatest_decrease_month) + "  $" + str(int(greatest_decrease)))
