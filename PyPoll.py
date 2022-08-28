# 1. The total nuimber of votes cast
# 2. A Complete list of candidate who orecieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of the election based on papular vote
# 5. The winner of the election based on popular vote
# Add our dependencies.
import csv
import os

file_to_load =os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)