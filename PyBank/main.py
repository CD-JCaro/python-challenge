import csv
import os

path = os.path.join("Resources" ,"budget_data.csv")
#opening file
with open(path, "r") as file:
    #initializing my variables
    numMonths = 0
    maxProfit = 0
    maxMonth = ""
    minProfit = 0
    minMonth = ""
    totalProfit = 0

    #reading it as a csb
    fileReader = csv.reader(file, delimiter = ',')

    #skipping header
    columns = next(fileReader)

    #for each element in the file
    for row in fileReader:
        #keepin track of our months and nabbing our current profit for this iteration
        numMonths = numMonths + 1
        profit = int(row[1])
        totalProfit = totalProfit + profit
        
        #seeing if we got min/max
        if(profit > maxProfit):
            
            maxProfit = profit
            maxMonth = row[0]

        elif(profit < minProfit):
            
            minProfit = profit
            minMonth = row[0]
        
    averageProfit = totalProfit / numMonths


    #print time
    print("")
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {numMonths}")
    print(f"Total Profit: {totalProfit}")
    print(f"Average Change: ${round(averageProfit, 2)}")
    print(f"Greatest Increase in Profits: {maxMonth} (${maxProfit})")
    print(f"Greatest Decrease in Profits: {minMonth} (${minProfit})")
    print("")

#export time
with open("Financial_Analysis.txt", "w+") as outFile:
    outFile.write("Financial Analysis\n")
    outFile.write("------------------\n")
    outFile.write(f"Total Months: {numMonths}\n")
    outFile.write(f"Total Profit: ${totalProfit}\n")
    outFile.write(f"Average Change: ${round(averageProfit, 2)}\n")
    outFile.write(f"Greatest Increase in Profits: {maxMonth} (${maxProfit})\n")
    outFile.write(f"Greatest Decrease in Profits: {minMonth} (${minProfit})\n")
    outFile.close()
