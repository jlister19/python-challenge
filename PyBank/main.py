import csv
import os

# Import the file, it will return a list of lists
budget_data_path = os.path.join('resources', 'budget_data.csv')

# Import the file, it will return a list of lists
election_data_path = os.path.join('resources', 'election_data.csv')

# read the file
with open(budget_data_path) as budget_data_file:
    reader = csv.reader(budget_data_file, delimiter=',')

    # Read the header row first
    csv_header = next(reader)

    tot_months = 0 # sets total month counter variable to 0
    total_profit = 0 # sets total profit counter variable to 0
    profit_deltas_list = [] # create empty list
    month_of_delta_list = [] # create empty list
    greatest_incr_list = [0,0] # create empty list with 2 zero values
    greatest_decr_list = [0,0] # create empty list with 2 zero values
 
	# makes sure first non-header row gets exluded from for loop
    first_row = next(reader) # create first row variable (first row after header)
    tot_months = tot_months + 1 # add 1 to total months variable 
    total_profit = total_profit + int(first_row[1]) # set total net variable = to Jan profit 
    prev_profit = int(first_row[1]) # set prev net variable = to Jan profit 

    for row in reader:

        # Accumulate totals to print at end
        tot_months = tot_months + 1 # add 1 to the total count of months variable
        total_profit = total_profit + int(row[1]) # add current month profit to total net variable

        # Accumulate profit deltas
        curr_profit = int(row[1]) - prev_profit # calc current month net change into a variable to add that will be appended to the profit_deltas_list list 
        prev_profit = int(row[1]) # immediately update the prev net variable to the current row's net 
        profit_deltas_list += [curr_profit] # append current month net change to the profit_deltas_list list
        month_of_delta_list += [row[0]] # append current month to the month of change list

        # Calculate greatest increase
        if curr_profit > greatest_incr_list[1]:
           greatest_incr_list[0] = row[0]
           greatest_incr_list[1] = curr_profit

        # Calculate greatest decrease
        if curr_profit < greatest_decr_list[1]:
           greatest_decr_list[0] = row[0]
           greatest_decr_list[1] = curr_profit

# Calc Avg Change in Profits
net_monthly_avg = sum(profit_deltas_list) / len(profit_deltas_list)

# print results to terminal 
print(f"Total Months: {tot_months}") 
print(f"Total: {total_profit}") 
print(f"Average Change: {net_monthly_avg}")
print(f"Greatest Increase in Profits: {greatest_incr_list[0]} {greatest_incr_list[1]}")
print(f"Greatest Decrease in Profits: {greatest_decr_list[0]} {greatest_decr_list[1]}")

# create the path text file to save results to  
text_file = os.path.join("analysis", "pybank_results.txt")

with open(text_file, "w") as out_file:
    out_file.writelines(["Financial Analysis \n",
                        "-------------------------- \n",
                        "Total Months: " + repr(tot_months) + "\n",
                        "Total: $" + repr(total_profit) + "\n",
                        "Average Change: $" + repr(net_monthly_avg) + "\n",
                        "Greatest Increase in Profits: " + repr(greatest_incr_list[0]) + " $" + repr({greatest_incr_list[1]}) + "\n"
                        "Greatest Decrease in Profits: " + repr(greatest_decr_list[0]) + " $" + repr({greatest_decr_list[1]}) + "\n"
                        ])

