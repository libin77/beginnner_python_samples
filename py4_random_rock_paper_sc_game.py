import random

# rock-paper-scissors
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


# print choice
def print_choice(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)


# choice
player_choice = int(input("Choose Rock(0), Paper(1), Scissors(2) : "))
print_choice(player_choice)
computer_choice = random.randint(0, 2)
print_choice(computer_choice)

# Rules
rules = [["Tie", "Wins", "Lose"], ["Wins", "Tie", "Lose"], ["Lose", "Wins", "Tie"]]

# Result
print(f"You {rules[player_choice][computer_choice]}")
