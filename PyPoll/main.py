import csv

with open("election_data.csv", newline = '') as file:
    nTotalVotes = 0

    dictCandidates = {}

    fileReader = csv.reader(file)

    columns = next(fileReader)

    for row in fileReader:
        nTotalVotes = nTotalVotes + 1
        dictCandidates[row[2]] = dictCandidates.setdefault(row[2], 0) + 1

    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {nTotalVotes}")
    print("------------------------")

    
    for candidate, votes in dictCandidates.items():
        print(f"{candidate}: {round((votes/nTotalVotes) * 100, 3)}% ({votes})")

    print("------------------------")
    print(f"Winner: {max(dictCandidates, key = dictCandidates.get)}")
    print("------------------------")

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