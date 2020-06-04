import os
import csv
import numpy

numMonth=0 #total number of months
profitLoss=0 #net total profit/loss
trackChange=[] #array containing change in profit/loss by month
maxProfitMth=[] #month with the greatest increase in profit
maxProfit=0 #greatest increase in profit
minProfitMth=[] #month with the greatest decrease in losses
minProfit=0 #greatest decrease in losses
value=0 #temporary storage for row's profit/loss, to be used in tracking change

filepath=os.path.join("Resources","budget_data.csv") #open file path
outfilepath=os.path.join("analysis","pybank.txt") #save output path

with open(filepath,"r") as pybank:
    pybankfile=csv.reader(pybank,delimiter=",")
    pybankheader=next(pybankfile) #ignore header
    for row in pybankfile:
        numMonth+=1 #increment number of months across row
        if numMonth > 1: #change in profit/loss can inly be calculated from 2nd month onwards
            trackChange.append(int(row[1])-value) #record change in profit
            if int(row[1])-value > maxProfit: #record month and value if change in profit is greater than previous change
                maxProfit=int(row[1])-value
                maxProfitMth=row[0]
            if int(row[1])-value < minProfit: #and vice versa
                minProfit=int(row[1])-value
                minProfitMth=row[0]
        value=int(row[1]) #update value to reflect current row's profit/change
        profitLoss=profitLoss+value #add profit/loss to the cumulative profit/loss

trackChange=numpy.array(trackChange) 
avgChange=numpy.sum(trackChange)/len(trackChange) #use numpy to get the average change in profit

report=f"Financial Analysis\n----------------------------\nTotal Months: {numMonth}\nTotal: \
${profitLoss}\nAverage Change: ${round(avgChange,2)}\nGreatest Increase in Profits: \
{maxProfitMth} (${maxProfit})\nGreatest Decrease in Profits: {minProfitMth} (${minProfit})"

print(report)

with open(outfilepath,"w") as output:
    output.write(report) #save output
    