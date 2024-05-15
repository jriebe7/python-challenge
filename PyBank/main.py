# Import os and csv
import os
import csv
from datetime import datetime

# set file path to open
csvpath = os.path.join("Resources", "budget_data.csv")

# open file and set delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


#   skip header data
    header = next(csvreader) 

    # create lists to differentiate data
    
    profit_date = []
    profit_loss = []

    
    # add data to lists
    for row in csvreader:
        profit_date.append(row[0])
        profit_loss.append(int(row[1]))
    
    chart = list(zip(profit_date, profit_loss))         

# **Task 1** - Calculate the total number of months in the dataset:

    total_months = str(len(profit_date))

    

# **Task 2** - Calculate the net total amount of "Profit/Losses" over the entire period:

    total_profit = sum(profit_loss)

    print("The net total of 'profit/losses' during this period was $" + str(total_profit))

# **Task 3** - Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes

    changes = []
        
    for i in range(1, len(profit_loss)):
        change = profit_loss[i] - profit_loss[i - 1]
        changes.append(change)
        average_change = round(sum(changes) / len(changes), 2)

    print("The average change in this data was $" + str(average_change))

# **Task 4 & 5** Find the greatest increase and decrease in profits (date and amount) over the entire period

    max_change = 0
    min_change = 0
    maxmonth_change = str(0)
    minmonth_change = str(0)
            
    for i in range(len(profit_loss)):
        change = profit_loss[i] - profit_loss[i - 1]
        if change >= max_change:
            max_change = change
            maxmonth_change = profit_date[i]
        if change <= min_change:
            min_change = change
            minmonth_change = profit_date[i]
        
    # Print results
    
    print("Financial Analysis")                  
          
    print("-------------------------------------")

    print("Total months: " + total_months)

    print("Total: $" + str(total_profit))

    print("Average Change: $" + str(average_change))

    print("Greatest Increase in Proifits: $" + str(max_change) + " " + "(" + maxmonth_change + ")")
    
    print("Greatest Decrease in Profits: $" + str(min_change) + " " + "(" + minmonth_change + ")")
        
    
    output_path = os.path.join("Analysis", "Financial_Analysis.csv")

    with open(output_path, 'w', newline="") as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(["-------------------------------------"])
        csvwriter.writerow(["Total months: " + total_months])
        csvwriter.writerow(["Total: $" + str(total_profit)])
        csvwriter.writerow(["Average Change: $" + str(average_change)])
        csvwriter.writerow(["Greatest Increase in Proifits: $" + str(max_change) + " " + "(" + maxmonth_change + ")"])
        csvwriter.writerow(["Greatest Decrease in Profits: $" + str(min_change) + " " + "(" + minmonth_change + ")"])
       


    















