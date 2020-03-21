#Pybank.py
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','budget_data.csv')



# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
        
    #initialize sum of profit_loss and number of months 
    sum_profit_loss = 0
    num_of_months = 0

    value = 0

    #initial value to calculate the difference in profit loss
    diff = 0
    month_list = []
    profit_loss = []

    for row in csvreader:
        print(row)

        # calculating number of months
        num_of_months = num_of_months + 1
        sum_profit_loss = sum_profit_loss + int(row[1])

        # Keep track of the month
        month_list.append(row[0])
        

        #calculating difference in profit/loss
        diff = int(row[1]) - value
        profit_loss.append(diff)
        value = int(row[1])

    #Have to exclude the first value since there is no change calculated
    avg_profit_loss = (sum(profit_loss)-profit_loss[0])/(len(profit_loss) -1 )
    #print("average profit/loss" + str(avg_profit_loss))
    #print(sum_profit_loss)
    #print(num_of_months)
    #print(month_list)
    #print((profit_loss))

    print(len(month_list))
    print(len(profit_loss))
    greatest_increase = max(profit_loss)
    index_of_greatest_increase = profit_loss.index(greatest_increase)
    #print("max value month is" + month_list[index_of_greatest_increase])
    mon_of_greatest_increase =month_list[index_of_greatest_increase]

    greatest_decrease = min(profit_loss)
    index_of_greatest_decrease = profit_loss.index(greatest_decrease)
    #print("min value month is" + month_list[index_of_greatest_decrease])
    mon_of_greatest_decrease =month_list[index_of_greatest_decrease]


    

    
    
#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(num_of_months)}")
print(f"Total: ${str(sum_profit_loss)}")
print(f"Average Change: ${str(round(avg_profit_loss,2))}")
print(f"Greatest Increase in Profits: {mon_of_greatest_increase} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {mon_of_greatest_decrease} (${str(greatest_decrease)})")

#Exporing to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(num_of_months)}")
line4 = str(f"Total: ${str(sum_profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_profit_loss,2))}")
line6 = str(f"Greatest Increase in Profits: {mon_of_greatest_increase} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {mon_of_greatest_decrease} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
        

    
    



    


