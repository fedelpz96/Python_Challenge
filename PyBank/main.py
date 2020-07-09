#Modules
import os
import csv

#Print title
print ('Finantial Analysis')
print ('----------------------------------')

#Set variables
Monthcount=0
Total=0
Increase=0
Increase_Max=0
Decrease=0
Decrease_Max=0
Prev=0

#Set path for file
csvpath = os.path.join("c:/Users/Fededo/Desktop/BootCamp/Tareas/Tarea_3/Python_Challenge/PyBank/Resources","Week 3 - Python_Homework_PyBank_Resources_budget_data.csv")

#Open with CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    #Loop through file and count the months, and add up the total
    for row in csvreader:
        Monthcount += 1
        Total = Total + int(row[1])
        Current = int(row[1])
        #Store values for Greatest Increase and Decrease
        if Prev >= int(row[1]):
            Decrease = Prev-int(row[1])
            if Decrease > Decrease_Max:
                Decrease_Max = Prev-int(row[1])
                DMD = row[0]
        if Prev <= int(row[1]):
            Increase = int(row[1])-Prev
            if Increase > Increase_Max:
                Increase_Max = int(row[1])-Prev
                IMD = row[0]
        Prev=int(row[1])

    #Calculate average
    Average = Total / Monthcount 
    #print results   
    print ("Total Months: " + str(Monthcount))
    print ("Total: $" + str(Total))
    print ("Average: $" + str(Average))
    print ("Greatest Increase in Profits: " + IMD + " $" + str(Increase_Max))
    print ("Greatest Decrease in Profits: " + DMD + " -$" + str(Decrease_Max))


#Create a new file with these results

#open new Results file
results = open("results.txt","w")
#write into new file
results.write('Finantial Analysis')
results.write('-------------------------')
results.write("Total Months: " + str(Monthcount))
results.write("Total: $" + str(Total))
results.write("Average: $" + str(Average))
results.write("Greatest Increase in Profits: " + IMD + " $" + str(Increase_Max))
results.write("Greatest Decrease in Profits: " + DMD + " -$" + str(Decrease_Max))
results.close()