# Import os and csv
import os
import csv
from collections import Counter

# set file path to open
csvpath = os.path.join("Resources", "election_data.csv")

# open file and set delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    votes = []
    candidate = []

    for row in csvreader:
        votes.append(row[0])
        candidate.append(row[2])

    total_votes = int(len(votes))
    vote_count = Counter(candidate)
    max_votes = max(vote_count.values())
    min_votes= min(vote_count.values())
    second_votes = total_votes - (max_votes + min_votes)
    percentage_max = round(max_votes/total_votes*100, 2)
    percentage_second = round(second_votes/total_votes*100, 2)
    percentage_third = round(min_votes/total_votes*100, 2)

    first = [i for i in vote_count.keys() if vote_count[i] == max_votes]
    last =  [i for i in vote_count.keys() if vote_count[i] == min_votes]
    second =  [i for i in vote_count.keys() if vote_count[i] != max_votes and vote_count[i] != min_votes]
   
    print("Total votes: " + str(total_votes))
    print("Winner: " + first[0] + " with " + str(max_votes) + " votes (" + str(percentage_max) + "%)")
    print("2nd place: " + second[0] + " with " + str(second_votes) + " votes (" + str(percentage_second) + "%)")
    print("3rd place: " + last[0] + " with " + str(min_votes) + " votes (" + str(percentage_third) + "%)")
    
    output_path = os.path.join("Analysis", "Election_Results.csv")

    with open(output_path, 'w', newline="") as csvfile:

    # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["--------------------------------"])
        csvwriter.writerow(["Total votes: " + str(total_votes)])
        csvwriter.writerow(["Winner: " + first[0] + " with " + str(max_votes) + " votes (" + str(percentage_max) + "%)"])
        csvwriter.writerow(["2nd place: " + second[0] + " with " + str(second_votes) + " votes (" + str(percentage_second) + "%)"])
        csvwriter.writerow(["3rd place: " + last[0] + " with " + str(min_votes) + " votes (" + str(percentage_third) + "%)"])


    # used counter function from method 2 here: https://www.geeksforgeeks.org/dictionary-counter-python-find-winner-election/
 
    

    


