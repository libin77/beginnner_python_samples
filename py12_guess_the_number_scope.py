import random

from art import logo_guess

#Number guessing game
EASY_LEVEL = 10
HARD_LEVEL = 5

print(logo_guess)
print("Welcome to the Number Guessing Game!")

def set_game_level():
  if input("choose a difficulty level (easy/hard): ").lower() == "easy":
    return EASY_LEVEL
  return HARD_LEVEL

def check_aswer(your_guess, computer_guess, life):
  """Get both guess and return the remaining turn"""
  if your_guess == computer_guess:
    print(f"You got it right, Answer is {computer_guess}")
    return life
    
  if your_guess > computer_guess:
    print("Too High")
  else:
    print("Too Low")

  return life - 1

def play_game():
  level = set_game_level()
  print("I'm thinking of a number between 1 and 100.")
  print(f"You have {level} attempts")
  computer_guess = random.randint(1,100)
  my_guess = 0
  while my_guess != computer_guess:
    my_guess = int(input("Make a guess: "))
    level = check_aswer(my_guess, computer_guess, level)
    if my_guess == computer_guess:
      return
    if level < 1:
      print(f"You Loose, No attempts remaining, answer was {computer_guess}")
      return
    print("Guess Again..")
    print(f"you have {level} attempts remaining")
    
play_game()

