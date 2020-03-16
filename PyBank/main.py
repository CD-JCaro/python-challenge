import csv

with open("budget_data.csv", newline = '') as file:
    numMonths = 0
    maxProfit = 0
    maxMonth = ""
    minProfit = 0
    minMonth = ""
    totalProfit = 0

    fileReader = csv.reader(file)

    columns = next(fileReader)

    for row in fileReader:
        
        numMonths = numMonths + 1
        profit = int(row[1])
        totalProfit = totalProfit + profit
        
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

with open("Financial_Analysis.txt", "w+") as outFile:
    outFile.write("Financial Analysis\n")
    outFile.write("------------------\n")
    outFile.write(f"Total Months: {numMonths}\n")
    outFile.write(f"Total Profit: ${totalProfit}\n")
    outFile.write(f"Average Change: ${round(averageProfit, 2)}\n")
    outFile.write(f"Greatest Increase in Profits: {maxMonth} (${maxProfit})\n")
    outFile.write(f"Greatest Decrease in Profits: {minMonth} (${minProfit})\n")
    outFile.close()
