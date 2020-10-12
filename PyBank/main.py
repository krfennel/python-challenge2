#bring in file types
import os
import csv
# import the file i'm working on
budgetData_csv = os.path.join('PyBank','Resources', 'budget_data.csv')

# what am I looking for - Total (months)
totalMonths = []
#print(totalMonths)

# net total of profit/losses - 
totalAmount = []
# past Amount -
amountVariance = 0
# amount variance
monthVariance = 0
profitLoss = int(budget_data.csv[1])

# create my loop so it continues to calculate through the data

with open(budgetData_csv) as bankData:
    csvreader = csv.reader(bankData, delimiter=',')

    csvheader = next(csvreader)
    for row in csvreader:

# Add the months
        totalMonths.append(row[0])
    print(f'Total Months: {len(totalMonths)}')

 # Add the amounts     
    totalAmount.append(row[1])
    print(f'Total Amount: {sum(totalAmount)}')

