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

import random

user_input= int(input("type 0 for rock, 1 for paper, 2 for scissors\n"))

if user_input == 0:
    print(rock)

elif user_input == 1:
    print(paper)

elif user_input == 2:
    print(scissors)

else:
    print("Invalid input")


computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print(f"computer_choice: {rock}")

elif computer_choice == 1:
    print(f"computer_choice: {paper}")

else:
    print(f"computer_choice: {scissors}")

#  Rock wins against scissors; paper wins against rock; and scissors wins against paper. #

if user_input == 0 and computer_choice == 2:
    print("you won")

elif user_input == 1 and computer_choice == 0:
    print("you won")

elif user_input == 2 and computer_choice == 1:
    print("you won")

elif user_input == computer_choice:
    print("It is a draw")

else:
    print("you lose")