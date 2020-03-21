# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

input_path = os.path.join('..', 'PyBank', 'budget_data.csv') #specify the file path to read from
output_path = os.path.join('..','PyBank','Text_Output.txt')  # specify the file to write to

total_months= 0 #to count total_months
prev_revenue = 0 # to calculate change in revenue by month
monthOfChange = [] #list to keep months showing change
revenueChangeList = [] #list to track the change of revenue ,so as to sum up later
revenueChange = 0 
total_ProfitLosses = 0 
#--------------------------------------------------------------------------------------

# Open the CSV file and create an object of it for iteration
with open(input_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row to compare changes in relative to rest 
    first_row = next(csvreader)
    total_months +=1
    total_ProfitLosses += int(first_row[1])
    prev_revenue = int(first_row[1])

#---------------------------------------------------------------------------------------

    # for second row and there on loop it till the end
    for row in csvreader:
        #keep the dates updated
        monthOfChange.append(row[0])

        #Calculate the revenue Change,then add it to the list of revenueChanges
        revenueChange = int(row[1]) - prev_revenue
        revenueChangeList.append(revenueChange)
        prev_revenue = int(row[1])

        #Total number of months
        total_months += 1
         
        #Total net amount of Profit/Losses over entire period
        total_ProfitLosses = total_ProfitLosses + int(row[1])

#-----------------------------------------------------------------------------------------  
#      
    # Average Change in Profit/Losses over the entire period
    Avg_Change = sum(revenueChangeList)/len(revenueChangeList)
    
    # Greatest Increase in Profits
    greatestIncrease = max(revenueChangeList)
    greatest_index = revenueChangeList.index(greatestIncrease)
    greatest_date = monthOfChange[greatest_index]

    # Greatest Decrease in Losses 
    greatestDecrease = min(revenueChangeList)
    lowest_index = revenueChangeList.index(greatestDecrease)
    lowest_date = monthOfChange[lowest_index]

#------------------------------------------------------------------------------------------
    

#Format the Output for Display
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Net amount of Profit/Losses Over Entire Period:   $ {total_ProfitLosses}\n"
    f"Average of changes in Profit/Losses Over Entire Period: $ {str(round(Avg_Change,2))}\n"
    f"Greatest Increase in Profits: {greatest_date}  ,  $ {str(greatestIncrease)}\n"
    f"Greatest Decrease in Losses : {lowest_date}  ,  $ {str(greatestDecrease)}\n")
 
 #Print OutPut to terminal
print(output)

#Export it to a text file
with open(output_path,"w") as textfile:
    textfile.write(output)