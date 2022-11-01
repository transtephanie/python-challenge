# Import dependencies
import os, csv

#Set/read the path for the CSV file
csvfile = '/Users/stephanietran/Desktop/python-challenge/pypoll.py/Resources/election_data.csv'

#Start total vote counter, variable, dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

#Tracking winner, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(csvfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row.
    headers = next(csvreader)

    #Print each row in the CSV file.
    for row in csvreader:
        #Add to the total vote count.
        total_votes += 1
        #Get the candidate name from each row.
        candidate_name = row[2]
        #If the candidate does not match any existing candidate, add the
        #the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
filepath = '/Users/stephanietran/Desktop/python-challenge/pypoll.py/analysis/mypollpyresults.txt'
with open(filepath, "w") as text_file:
    election_results = ("Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    text_file.write(election_results)
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        text_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    text_file.write(winning_candidate_summary)       