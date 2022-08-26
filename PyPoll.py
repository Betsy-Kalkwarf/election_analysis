
#The data we need to retrieve
import csv

import os
from pickle import APPEND

# Assign a variable to load a file from a path.
file_to_load = '/Users/Betsy/Desktop/UCSD Bootcamp/Unit 2 Python/election_analysis/Resources/election_results.csv'


# Assign a variable to save the file to a path.
file_to_save = '/Users/Betsy/Desktop/UCSD Bootcamp/Unit 2 Python/election_analysis/Resources/election_analysis.txt'
  
# Initialize variables (total votes as integer, candidates as list, candidate and votes as dictionary)
total_votes = 0
candidate_options = []
candidate_votes = {}

#Winning variables initailized
winning_candidate = " "
winning_count = 0
winning_percentage = 0


#Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    #print candidate name from each row
    for row in file_reader:

        #2. Get candidate names
        
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add vote for candidate and total votes
        candidate_votes[candidate_name] += 1
        total_votes += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.   
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.    
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100


        # Print the candidate name, numb of votes and percentage of votes.
        print(f"{candidate_name}:  {vote_percentage:.1f}% ({votes})\n")   

        # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
             # If true then set winning_count = votes and winning_percent =
             # vote_percentage.
             winning_count = votes  
             winning_percentage = vote_percentage
             # And, set the winning_candidate equal to the candidate's name.
             winning_candidate = candidate_name

#  print winning candidate, vote count and percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)






