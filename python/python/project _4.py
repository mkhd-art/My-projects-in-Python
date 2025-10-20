rock_ascii = """
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_ascii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
Game = [rock_ascii, paper_ascii, Scissors_ascii]
import random

# Welcome message
print("Welcom to: Rock, Paper, Scissors game:")
Answer = input("press enter to continue... or enter (Help) to know the ruls:").lower()
if Answer == "help":
  print("""         *****Rules*****
(1) you choose and the computer chooses
(2) Rock smashes scissors -> Rock wins
(3) Scissors cut paper -> Scissors wins
(4) Paper covers Rock -> Paper wins
""")
# user choice
user_choice = input("Enter your chice: (Rock, Paper, Scissors):").capitalize()
if user_choice not in ["Rock", "Paper", "Scissors"] :
 print("Invalid choice. please choose Rock, Paper, or Scissors.")
else :
  if user_choice == "Rock":
    print(f"your choice is : \n{rock_ascii}")
  elif user_choice == "Paper" :
    print(f"your choice is : \n{paper_ascii}")
  else : 
    print(f"your choice is : \n{Scissors_ascii}")

# computer choice
computer_choice = random.choice(["Rock", "Paper", "Scissors"])
if computer_choice == "Rock" :
  print(f"The computer choice is : \n{rock_ascii}")
elif computer_choice == "Paper" :
  print(f"The computer choice is : \n{paper_ascii}")
else :
  print(f"The computer choice : \n{Scissors_ascii}")

# determine the winner
if user_choice == computer_choice :
  print("It's a tie!\n Try again")
elif (
  (user_choice == "Rock" and computer_choice == "Scissors") or
  (user_choice == "paper" and computer_choice == "Rock") or
  (user_choice == "Scissors" and computer_choice == "paper") ):
  print(f"you win! {user_choice} beats {computer_choice}.")
else :
  print(f"you lose! {computer_choice} beats {user_choice}.")