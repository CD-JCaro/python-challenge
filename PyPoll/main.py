import csv
import os

path = os.path.join("Resources" ,"election_data.csv")

#opening our file
with open(path) as file:
    nTotalVotes = 0

    #getting my dict ready
    dictCandidates = {}

    fileReader = csv.reader(file)

    #keepin that header
    columns = next(fileReader)

    #looping through my elements
    for row in fileReader:
        #keepin track of my total votes
        nTotalVotes = nTotalVotes + 1

        #modifying the current count for our candidate... if there is no value we default it to 0
        dictCandidates[row[2]] = dictCandidates.setdefault(row[2], 0) + 1

    print("\nElection Results")
    print("------------------------")
    print(f"Total Votes: {nTotalVotes}")
    print("------------------------")

    #looping through our candidates and printing their name and total votes
    for candidate, votes in dictCandidates.items():
        print(f"{candidate}: {round((votes/nTotalVotes) * 100, 3)}% ({votes})")

    print("------------------------")
    print(f"Winner: {max(dictCandidates, key = dictCandidates.get)}")
    print("------------------------")

    #output time
    with open("Election_Results.txt", "w+") as outFile:
        outFile.write("Election Results\n")
        outFile.write("------------------------\n")
        outFile.write(f"Total Votes: {nTotalVotes}\n")
        outFile.write("------------------------\n")

        for candidate, votes in dictCandidates.items():
            outFile.write(f"{candidate}: {round((votes/nTotalVotes) * 100, 3)}% ({votes})\n")

        outFile.write("------------------------\n")
        outFile.write(f"Winner: {max(dictCandidates, key = dictCandidates.get)}\n")
        outFile.write("------------------------\n")

        outFile.close()