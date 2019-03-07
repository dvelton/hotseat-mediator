#Welcome screen
print("")

print("Welcome to Hotseat Mediator.")

print("")

print("This program will determine if there is a number at which the parties are willing to settle the case.")

print("")

print("Both sides can indicate acceptance or rejection of a number without fear of losing bargaining position. If one side rejects a particular number, it will never know whether the other side accepted or rejected that number. It is in both parties' interest to be honest with themselves. You do not benefit from posturing or artificially inflating or deflating demands/offers in this program. If you are willing to accept a number, indicate so or else you may skip over the window of opportunity and the number at which a case can settle.")

print("")

#Setting up range for the program
starting_number = int(input("Please agree on a starting dollar figure for the range and enter it here: $"))

final_number = int(input("Please agree on an ending dollar figure for the range and enter it here: $"))

interval_skip = int(input("Please agree on an interval for each jump between your starting and ending dollar figures: $"))

print("")

print("We will see if this case can settle somewhere between ${} and ${} at intervals of ${}. To indicate acceptance of a particular number, type Y or Yes or Accept. To indicate rejection of a particular number, type N or No or Reject. Take turns and do not view each other's answers.".format(starting_number, final_number, interval_skip))

print("")

#Setting up the loop  
neg = ["n", "no", "reject"]

pos= ["y", "yes", "accept"]

for i in range(starting_number, final_number + 1, interval_skip):

    plaintiff_response = input("Plaintiff: what is your response to $" + str(i) + "? ")
    
    print("\n" * 250)
    
    defendant_response = input("Defendant: what is your response to $" + str(i) + "? ")
    
    print("\n" * 250)

    if plaintiff_response.lower() in neg or defendant_response.lower() in neg:
        
        continue
    
    elif i == final_number:
        
        break

    elif plaintiff_response.lower() in pos and defendant_response.lower() in pos:
        
        break
            
if plaintiff_response.lower() in pos and defendant_response.lower() in pos:    
    
    print("")
            
    print("Congratulations! Both sides are willing to settle the case at $" + str(i) + ".")
    
elif plaintiff_response.lower() in neg or defendant_response.lower() in neg:
    
    print("")
    
    print("Unfortunately it does not appear the parties have any common ground.") 
