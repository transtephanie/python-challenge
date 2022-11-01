#Import dependencies for os.path.join()
import os
import csv

#Set/read the path for the CSV file
#csvpath = os.path.join("..", "Resources", "budget_data.csv")
csvfile = '/Users/stephanietran/Desktop/python-challenge/pybank.py/Resources/budget_data.csv'

#Create list to store data
total_months = []
total_profit = []
profit_change = []

#Open and read CSV
with open(csvfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header to iterate with the values
    header = next(csvreader)

    #Iterate through each row of data 
    for row in csvreader:

        #Add date 
        total_months.append(row[0])

        #Add Profit
        total_profit.append(int(row[1]))
    
    #Iterate through profits to get monthly change in profits
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-total_profit[i])

#Calculate greatest increase in profits (date and amount)
greatest_increase = max(profit_change)

#Calcuate greatest decrease in loss (date and amount)
greatest_decrease = min(profit_change)

greatest_increase_month = profit_change.index(max(profit_change))+1
greatest_decrease_month = profit_change.index(min(profit_change))+1

#Print Financial Analysis statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")

#Print Financial Analysis and export to a text file
#Set path for file
filepath = '/Users/stephanietran/Desktop/python-challenge/pybank.py/analysis/mypybankresults.txt'
with open(filepath, "w") as text_file:
    output_text = ("Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {len(total_months)}\n"
    f"Total: ${sum(total_profit)}\n"
    f"Average Change: {round(sum(profit_change)/len(profit_change), 2)}\n"
    f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})\n"
    f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})\n")
    text_file.write(output_text)