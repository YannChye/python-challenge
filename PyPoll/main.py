import os
import csv

totalVotes=0 #total votes cast
candidate={} #dictionary list of candidates, with each element representing name-vote pair
percentVote=[] #percentage of votes by candidate
maxVote=0 #winning number of votes
maxVoteName="" #winning candidate

filepath=os.path.join("Resources","election_data.csv") #open file path
outfilepath=os.path.join("analysis","pypoll.txt") #save output path

with open(filepath,"r") as pypoll:
    pypollfile=csv.reader(pypoll,delimiter=",")
    pypollheader=next(pypollfile) #ignore header
    for row in pypollfile:
        totalVotes+=1 #increment number of votes down the row
        if row[2] not in candidate: #if candidate name is new, gets recorded as 
        #new item in dict with a starting value of 1 vote
            candidate[row[2]]=1
        elif row[2] in candidate: #if candidate name already exist, increment number of votes
            candidate[row[2]]=candidate[row[2]]+1

reportline="" #line in report denoting each candidate's outcome
for idx,name in enumerate(candidate):
    percentVote.append(0) #increase size of percentVote array to match number of candidates
    percentVote[idx]=candidate[name]/int(totalVotes)*100 #calculate percentVote for each candidate
    if candidate[name]>maxVote: #check for most voted for candidate
        maxVote=candidate[name]
        maxVoteName=name
    reportline=reportline+f"{name}: {format(percentVote[idx],'.3f')}% ({candidate[name]})\n"

reportline=reportline[:-1] #remove '\n' newline from the last candidate
report=f"Election Results\n-------------------------\nTotal \
Votes: {totalVotes}\n-------------------------\n{reportline}\
\n-------------------------\nWinner: {maxVoteName}\n-------------------------"

print(report)

with open(outfilepath,"w") as output:
    output.write(report)