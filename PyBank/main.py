# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Define variables to track the financial data
count = 0
total = 0
first = 0
last = 0
diff = 0
diff_min = 0
diff_min_date = ""
diff_max = 0
diff_max_date = ""

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Open and Read the file line by line
with open(file_to_load) as f:
    csvreader = csv.reader(f)
    
    # Skip the header row
    next(csvreader)
    
    # Read file line by line and count the number of lines
    # Keep track of minimum diff and maximum diff and corresponding dates  
    for line in csvreader:
        count = count + 1
        total = total + int(line[1])
        diff = int(line[1]) - last
        if diff < diff_min:
            diff_min = diff
            diff_min_date = line[0]
        if diff > diff_max:
            diff_max = diff
            diff_max_date = line[0]
        last = int(line[1])
        if first == 0:
            first = int(line[1])

    # Calculate average           
    average = (last-first)/(count-1)
    
    # Render output
    output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average:.2f}\n"
    f"Greatest Increase in Profits: {diff_max_date} (${diff_max})\n"
    f"Greatest Decrease in Profits: {diff_min_date} (${diff_min})\n"
    )
    print(output)

    # Save output to txt file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)