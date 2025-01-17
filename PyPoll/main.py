# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

input_path = os.path.join('..', 'PyPoll', 'election_data.csv') #specify the file path to read from
output_path = os.path.join('..','PyPoll','Text_Output.txt')  # specify the file to write to

#---------------------Define Variables-------------------------------------

Candidates = []         # List of Candidate names
Candidate_Votes = []    # Number of Votes each Candidate gets 
Percentage_Votes = []   # Percentage of Total votes each Candidate gets
total_votes = 0         # Total number of Votes

#----------------Open and Read the CSV file header---------------------------

with open(input_path,newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    #-----------------Loop through the rest of CSV file----------
    
    for row in csvreader:
        total_votes += 1 # Start Counting Votes 
        
        # Add Candidate (if not in the list already) and his respective Votes 
        # Calculate the Votes each Candidate gets 

        if row[2] not in Candidates:
            Candidates.append(row[2])
            serial = Candidates.index(row[2])
            Candidate_Votes.append(1)
        else:
            serial = Candidates.index(row[2])
            Candidate_Votes[serial] += 1 

    #--------------Calculate the Percentage of Votes each Candidate gets-----
    
    for votes in Candidate_Votes:
        Percentage = (votes/total_votes) * 100
        Percentage = round(Percentage)
        Percentage = "%.3f%%" % Percentage 
        Percentage_Votes.append(Percentage)


    #---------------- Decide on the Winner------------------

    Winner = max(Candidate_Votes)
    serial = Candidate_Votes.index(Winner)
    WinnerName = Candidates[serial]


#--------Format the Output for Display and Write to File------------
with open(output_path,"w") as textfile:
    
    Heading= (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {str(total_votes)}\n"
        f"--------------------------\n")
    print(Heading, end = "")
    textfile.write(Heading) 
    
    
    for i in range(len(Candidates)):
        Voter_Stats = f"{Candidates[i]}: {str(Percentage_Votes[i])} ({str(Candidate_Votes[i])})\n"
        print(Voter_Stats, end ="")
        textfile.write(Voter_Stats)

    who_Won = (
    f"--------------------------\n"
    f"Winner: {WinnerName}\n"
    f"--------------------------\n")
    print(who_Won)
    textfile.write(who_Won)



