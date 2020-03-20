# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

# Variables to track
total_months= 0 #to count total_months
prev_revenue = 0 # to calculate change in 
monthOfChange = []
revenueChangeList= []
greatestIncrease = ["",0] # create place holders for date of change and Greatest Increase in Profit
greatestDecrease = ["",99999999999999]
total_ProfitLosses = 0

# Since the CSV file can be comprehended as KEY-VALUE (names of column:Values of Data) pairs of a dictionary.
# the csv.DictReader() returns a dictionary for each row read off of the CSV file . 
with open(csvpath) as csvfile:
    # create an object of the csv_DictReader() which can be iterated using a for loop
    looper = csv.DictReader(csvfile)

    for row in looper:
        #count total months and total revenue
        total_months=total_months + 1
        total_revenue=total_revenue + int(row["Profit/Losses"])

        #track the change in revenue
        revenue_change = int(row["Profit/Losses"])-prev_revenue
        pre_revenue = int(row["Profit/Losses"])
        revenueChangeList = revenueChangeList + [revenue_change]
        monthOfChange = monthOfChange + [row["Date"]]
