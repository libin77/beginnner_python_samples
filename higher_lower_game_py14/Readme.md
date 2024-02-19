# Higher Lower Game

This is a simple Higher Lower game where the player compares the number of followers between two randomly selected celebrities and tries to guess who has more followers.

## How to Play

1. Upon starting the game, the player is presented with two randomly chosen celebrities.
2. The player is shown the name, description, and country of each celebrity.
3. The player then selects their choice by typing 'A' if they think the first celebrity has more followers or 'B' if they think the second celebrity has more followers.
4. If the player's guess is correct, their score increases by 1, and a new comparison is made with the second celebrity becoming the first one. If the player's guess is incorrect, the game ends.
5. The game continues until the player guesses incorrectly.

## Code Overview

- The `random_game_data()` function selects a random celebrity from the provided data.
- The `construct_sentence()` function constructs a string representing a celebrity's name, description, and country.
- The `display_players()` function prints out the information of the two celebrities for the player to compare.
- The `is_game_over()` function checks whether the game should continue based on the player's choice and the current scores.
- The `start_game()` function initializes the game, manages the game loop, and keeps track of the player's score.

## External Dependencies

- `random`: Python standard library for generating random numbers.
- `replit`: A library for clearing the console screen.
- `art`: A custom module providing ASCII art for the game's logo and vs separator.
- `game_data`: A custom module containing data about celebrities.

## Running the Game

1. Ensure all external dependencies are installed.
2. Run the script, and the game will start automatically.
