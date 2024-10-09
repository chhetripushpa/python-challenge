import csv
import os
csvpath = os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")
with open(csvpath) as f:
    csvreader = csv.reader(f)
    next(csvreader)
    count = 0
    total = 0
    first = 0
    last = 0
    diff = 0
    diff_min = 0
    diff_min_date = ""
    diff_max = 0
    diff_max_date = ""
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
    average = (last-first)/(count-1)
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
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)