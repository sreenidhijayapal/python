rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

numbers = [0, 1, 2]
#print(random.choice(numbers))
user_choice = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors\n"))
print(f"User chose {user_choice}")

#print ASCII of game gesture
game_gesture = [rock, paper, scissors]
if user_choice in range(0, 3):
    print(game_gesture[user_choice])

#python switch statement
"""
def func(user_choice):
  match (user_choice):
    case 0:
      print(rock)
    case 1:
      print(paper)
    case 2:
      print(scissors)
"""
comp_choice = int(random.choice(numbers))
print(f"Computer chose {comp_choice}")

print(game_gesture[comp_choice])

#game rules
if user_choice >= 3 or user_choice < 0:
    print("The number is invalid, you lose.")
elif user_choice == 0 and comp_choice == 2:
    print("You won! :)")
elif user_choice == 2 and comp_choice == 0:
    print("You lost! :(")
elif user_choice > comp_choice:
    print("You won! :)")
elif user_choice < comp_choice:
    print("You lost! :(")
elif user_choice == comp_choice:
    print("It's a draw")
