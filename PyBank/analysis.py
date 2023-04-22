# %%

import os
import csv

csvpath = os.path.join("PyBank","Resources", "budget_data.csv")
print(csvpath)

# %%
total_months = 0
total_profit_losses = 0
previous_profit_losses = None
changes_in_profit_losses = []
greatest_increase_date = None
greatest_increase_amount = 0
greatest_decrease_date = None
greatest_decrease_amount = 0

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])
        
        total_months += 1
        
        total_profit_losses += profit_losses
        
        if previous_profit_losses is not None:
            change_in_profit_losses = profit_losses - previous_profit_losses
            changes_in_profit_losses.append(change_in_profit_losses)
            
            if change_in_profit_losses > greatest_increase_amount:
                greatest_increase_date = date
                greatest_increase_amount = change_in_profit_losses
            elif change_in_profit_losses < greatest_decrease_amount:
                greatest_decrease_date = date
                greatest_decrease_amount = change_in_profit_losses
        
        previous_profit_losses = profit_losses

average_change_in_profit_losses = sum(changes_in_profit_losses) / len(changes_in_profit_losses)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change_in_profit_losses:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Average Change: ${average_change_in_profit_losses:.2f}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")
   
