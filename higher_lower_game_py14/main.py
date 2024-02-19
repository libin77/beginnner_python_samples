import random

from replit import clear

from art import logo, vs
from game_data import data

def random_game_data():
  """Generate random game data"""
  return random.choice(data)

def construct_sentence(chosen_celeb):
  """Construct or format chosen player dictionary"""
  return f"{chosen_celeb['name']}, a {chosen_celeb['description']} from {chosen_celeb['country']}"

def display_players(compareA,compareB):
  """Display two different data to compare"""
  print(f"Compare A: {construct_sentence(compareA)}")
  print(vs)
  print(f"Compare B: {construct_sentence(compareB)}")

def is_game_over(score_a, score_b, player_choice):
  """Check if player guess correct and return"""
  if player_choice.lower() == "a" and score_a > score_b:
    return False
  if player_choice.lower() == "b" and score_a < score_b:
    return False
  return True

def start_game():
  """Entry point"""
  score = 0
  display_msg = "Current Score"
  compareA = random_game_data()
  compareB = random_game_data()
  
  game_over = False
  while not game_over:
    clear()
    print(logo)
    print(f"{display_msg}: {score}")
    display_players(compareA, compareB)
    player_choice = input("Who has more followers? Type 'A' or 'B': ")
    game_over = is_game_over(compareA['follower_count'], compareB['follower_count'], player_choice)
    if not game_over:
      score += 1
      if player_choice.lower() == "b":
        compareA = compareB
      compareB = random_game_data()
      display_msg = "You are right! Current Score"
    
  print(f"Game Over! Your final Score: {score}")
  
start_game()
