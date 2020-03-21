# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

input_path = os.path.join('..', 'PyBank', 'budget_data.csv') #specify the file path to read from
output_path = os.path.join('..','PyBank','Text_Output.txt')  # specify the file to write to

# Variables to track
total_months= 0 #to count total_months
prev_revenue = 0 # to calculate change in revenue by month
monthOfChange = [] #list to keep months showing change
revenueChangeList= [] #list to track the change of revenue 
greatestIncrease = ["",0] # create a List with place holders for date of change and amount
greatestDecrease = ["",99999999999999] # # create a List with place holders for date of change and amount
total_ProfitLosses = 0 

# Since the CSV file can be comprehended as KEY-VALUE (names of column:Values of Data) pairs of a dictionary.
# the csv.DictReader() returns a dictionary for each row read of the CSV file . 
with open(input_path) as csvfile:
    # create an object of the csv_DictReader() which can be iterated using a for loop
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        #count total months and total revenue
        total_months=total_months + 1
        total_revenue=total_revenue + int(row["Profit/Losses"])

        #track the change in revenue
        revenue_change = int(row["Profit/Losses"])- prev_revenue
        pre_revenue = int(row["Profit/Losses"])
        revenueChangeList = revenueChangeList + [revenue_change]
        monthOfChange = monthOfChange + [row["Date"]]

        #Calculate the Greatest Increase in Profit
        if(revenue_change>greatestIncrease[1]):
            greatestIncrease[0]=row["Date"]
            greatestDecrease[1]=revenue_change

        #Calculate the Greatest Decrease in Losses
        if(revenue_change<greatestDecrease[1]):
            greatestDecrease[0]=row["Date"]
            greatestDecrease[1]=revenue_change

# Calculate the AverageChange in Profit/Losses for the entire period
Avg_Change = sum(revenueChangeList)/len(revenueChangeList) #changes/number of times its changed 

#Output Format
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Net amount of Profit/Losses Over Entire Period: ${total_ProfitLosses}\n"
    f"Average of changes in Profit/Losses Over Entire Period:${Avg_Change}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]}  (${greatestIncrease[1]})\n"
    f"Greatest Decrease in Losses : {greatestDecrease[0]}  (${greatestDecrease[1]})\n")
 
 #Print OutPut to terminal
print(output)

#Export it to a text file
with open(output_path,"w") as textfile:
    textfile.write(output)

