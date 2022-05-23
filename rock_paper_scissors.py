import random, math



user_wins = 0
computer_wins = 0
number_of_rounds = int(input("Type how many rounds you would like to play (please enter a number): "))
round = 0 

if number_of_rounds == math.nan:
    print("Please enter a number next time")
    quit()
      


options = ["rock", "paper", "scissors"]

while round != number_of_rounds:
   user_input = input("Type rock, paper, or scissors - or type q to quit: ").lower()
   if user_input == "q":
      break
   
   if user_input not in options:
       continue  
   
   random_number = random.randint(0,2)
   # rock: 0, paper: 1, scissors: 2
   computer_pick = options[random_number]
   print("Computer picked", computer_pick + ".")
   
   if user_input == "rock" and computer_pick == "scissors":
       print("You won!")
       user_wins += 1
       round += 1
    
   elif user_input == "rock" and computer_pick == "rock":
       print("You tied!")
       user_wins += 1
       computer_wins += 1
       round += 1
       
   elif user_input == "paper" and computer_pick == "rock":
       print("You won!")
       user_wins += 1
       round += 1
       
   elif user_input == "paper" and computer_pick == "paper":
       print("You tied!")
       user_wins += 1
       computer_wins += 1
       round += 1
       
   elif user_input == "scissors" and computer_pick == "paper":
       print("You won!")
       user_wins += 1
       round += 1
       
   elif user_input == "scissors" and computer_pick == "scissors":
       print("You tied!")
       user_wins += 1
       computer_wins += 1
       round += 1
       
   else: 
       print("You lost!")
       computer_wins += 1
       round += 1
       
if user_wins == 1:
    print("You've won", user_wins, "time!")   
else: 
    print("You've won", user_wins, "times!")    

if computer_wins == 1:
    print("The computer has won", computer_wins, "time!")   
else: 
    print("The computer has won", computer_wins, "times!") 
        
  
     
print("Goodbye!")