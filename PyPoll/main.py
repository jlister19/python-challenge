import csv
import os

# Import the file, it will return a list of lists
election_data_path = os.path.join('resources', 'election_data.csv')

with open(election_data_path) as election_data_file:
    reader = csv.reader(election_data_file, delimiter=',')

    # Read the header row first
    csv_header = next(reader)
    
    tot_votes = 0 # sets total vote counter variable to 0
    unique_candidate_list = []     
    non_unique_candidate_list = []
 
 	# makes sure first non-header row gets exluded from the for loop
    first_row = next(reader) # create first row variable (first row after header)
    candidate = first_row[2]
    non_unique_candidate_list = [candidate]
    unique_candidate_list = [candidate]

    for row in reader:

#         # Accumulate totals to print at end
        tot_votes = tot_votes + 1 # add 1 to the total count of months variable

        candidate = row[2]
        non_unique_candidate_list += [candidate]
        if candidate not in unique_candidate_list:
             unique_candidate_list += [candidate]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {tot_votes}") 
print("-------------------------")

# initiate the cand name variable to be used in the below for loop
cand_name = unique_candidate_list[0]

# set the initial winner variable to the current candiate name before we enter the for loop. this variable doesn't iterate due to the below error (lines 48-51)
winner = cand_name

# for each unique candidate name, show the count of each time their name appears in the non_unique dataset (eg. count their votes) 
for cand_name in range(len(unique_candidate_list)):
    print(f"{unique_candidate_list[cand_name]}:  {round(non_unique_candidate_list.count((unique_candidate_list[cand_name])) / tot_votes * 100,4)}%  ({non_unique_candidate_list.count((unique_candidate_list[cand_name]))})")

###########line 1 of below code (intended to find the overal winner) causes a "Exception has occurred: TypeError" error
#   if non_unique_candidate_list.count((unique_candidate_list[cand_name])) > non_unique_candidate_list.count((unique_candidate_list[winner])):
#        winner = unique_candidate_list[cand_name]
###########above code intended to keep the winner name causes a "Exception has occurred: TypeError" error

# I was not able to a) resolve the below error or b) output the results to txt file. Ran out of time. Would love  suggestions

print("-------------------------")
print(f"Winner:  {winner}")
print("-------------------------")
