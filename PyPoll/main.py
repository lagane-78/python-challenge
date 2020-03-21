#Pybank.py
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','election_data.csv')



# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
        
    # intializing number of votes
    num_of_votes = 0

    #creating a dictionary of the candidates with number of votes initialized to 0, i am sure this can be done programmatically too
    # will have to try in my copious spare time
    candidate_dict = {
  "Khan": 0,
  "Correy": 0,
  "Li": 0,
  "O'Tooley":0
}

    for row in csvreader:
        #print(row)
        num_of_votes = num_of_votes + 1
        candidate_dict[row[2]] = candidate_dict[(row[2])]+1
    #print(str(num_of_votes))
    
    #print(candidate_dict)

    # calculate winner, find the maximum value for the number of votes
    all_values = candidate_dict.values()
    max_value = max(all_values)
    #print(max_value)

    # using list comprehension to find the key that corresponds to the maximum number of votes
    winner = []
    winner =([k for k,v in candidate_dict.items() if v == max_value])
    #print("winner is: "+ winner[0])

    print("Election Results")
    print("---------------------------------")
    print("Total Votes: " + str(num_of_votes))
    print("---------------------------------")
    print("Khan :"  + " " + '{:.1%}'.format(candidate_dict["Khan"]/num_of_votes) + " (" + str(candidate_dict["Khan"]) +")")
    print("Correy :" + " " +'{:.1%}'.format(candidate_dict["Correy"]/num_of_votes) + " (" +str(candidate_dict["Correy"]) +")")
    print("Li :" +" " + '{:.1%}'.format(candidate_dict["Li"]/num_of_votes)+ " (" + str(candidate_dict["Li"]) +")")
    print("O'Tooley :" + " " +'{:.1%}'.format(candidate_dict["O'Tooley"]/num_of_votes) + " (" + str(candidate_dict["O'Tooley"])  +")")
    print("---------------------------------")
    print("Winner is: "+ winner[0])
    print("---------------------------------")

    output = open("election_results_output.txt", "w")

    line1 = "Election Results"
    line2 = "---------------------------------"
    line3 = "Total Votes: " + str(num_of_votes)
    line4 = "--------------------------------"
    line5 = "Khan :"  + " " + '{:.1%}'.format(candidate_dict["Khan"]/num_of_votes) + " (" + str(candidate_dict["Khan"]) +")"
    line6 = "Correy :" + " " +'{:.1%}'.format(candidate_dict["Correy"]/num_of_votes) + " (" +str(candidate_dict["Correy"]) +")"
    line7 = "Li :" +" " + '{:.1%}'.format(candidate_dict["Li"]/num_of_votes)+ " (" + str(candidate_dict["Li"]) +")"
    line8 = "O'Tooley :" + " " +'{:.1%}'.format(candidate_dict["O'Tooley"]/num_of_votes) + " (" + str(candidate_dict["O'Tooley"])  +")"
    line10= "Winner is: "+ winner[0]
    line11 ="testing"
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line4,line10,line4))
            

    
    