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


def display_players(compare_a, compare_b):
    """Display two different data to compare"""
    print(f"Compare A: {construct_sentence(compare_a)}")
    print(vs)
    print(f"Compare B: {construct_sentence(compare_b)}")


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
    compare_a = random_game_data()
    compare_b = random_game_data()

    game_over = False
    while not game_over:
        clear()
        print(logo)
        print(f"{display_msg}: {score}")
        display_players(compare_a, compare_b)
        player_choice = input("Who has more followers? Type 'A' or 'B': ")
        game_over = is_game_over(compare_a['follower_count'], compare_b['follower_count'], player_choice)
        if not game_over:
            score += 1
            if player_choice.lower() == "b":
                compare_a = compare_b
            compare_b = random_game_data()
            display_msg = "You are right! Current Score"

    print(f"Game Over! Your final Score: {score}")


start_game()
