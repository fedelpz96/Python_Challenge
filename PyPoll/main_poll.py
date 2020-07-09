#Modules
import os
import csv

#Print title
print ('Election Results')
print ('----------------')

#Set path for file
csvpath = os.path.join("c:/Users/Fededo/Desktop/BootCamp/Tareas/Tarea_3/Python_Challenge/PyPoll/Resources","Week 3 - Python_Homework_PyPoll_Resources_election_data.csv")

#Assign variables
Votes = 0
KhanV = 0
CorreyV = 0
LiV = 0
OTooleyV = 0

#Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader (csvfile, delimiter=",")
    next(csvreader)
    #Loops through file to get required data
    for row in csvreader:
        Votes += 1
        #Count candidates votes
        if row[2] == "Khan":
            KhanV += 1
        if row[2] == "Correy":
            CorreyV += 1
        if row[2] == "Li":
            LiV += 1
        if row[2] == "O'Tooley":
            OTooleyV += 1
    #find the winner
    if KhanV > LiV and CorreyV and OTooleyV:
        Winner = "Khan"
    elif CorreyV > LiV and OTooleyV:
        Winner = "Correy"
    elif LiV > OTooleyV:
        Winner = "Li"
    else:
        Winner = "O'Tooley"
    
    #Calculate percentages and format as percentage with 2 decimals
    KhanP = "{:.2%}".format(KhanV/Votes)
    CorreyP = "{:.2%}".format(CorreyV/Votes)
    LiP = "{:.2%}".format(LiV/Votes)
    OToP = "{:.2%}".format(OTooleyV/Votes)

    #print colected data
    print ('Total votes: ' + str(Votes))
    print ('----------------')
    print ("Correy: " + str(CorreyP) + " " + str(CorreyV))
    print ("Khan: " + str(KhanP) + " " + str(KhanV))
    print ("Li: " + str(LiP) + " " + str(LiV))
    print ("O'Tooley: " + str(OToP) + " " + str(OTooleyV))
    print ("----------------")
    print ("Winner: " + Winner)

#create results file
results = open("results.txt","w")
#write into file
results.write ('Total votes: ' + str(Votes))
results.write ('----------------')
results.write ("Correy: " + str(CorreyP) + " " + str(CorreyV))
results.write ("Khan: " + str(KhanP) + " " + str(KhanV))
results.write ("Li: " + str(LiP) + " " + str(LiV))
results.write ("O'Tooley: " + str(OToP) + " " + str(OTooleyV))
results.write ("----------------")
results.write ("Winner: " + Winner)
results.close()
