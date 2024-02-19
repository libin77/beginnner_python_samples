# Hangman Game

This is a simple Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player has to guess the letters of the word one by one. The player has a limited number of lives, and with each incorrect guess, they lose a life. The game continues until the player correctly guesses the word or runs out of lives.

## How to Play

1. Run the Python script `main.py`.
2. The game will display the Hangman logo and the initial state of the word with underscores representing each letter.
3. Enter a letter as your guess when prompted.
- If the letter is correct, it will fill in the corresponding blanks.
- If the letter is incorrect, you lose a life, and a part of the Hangman is drawn.
4. Continue guessing letters until you either correctly guess the word or run out of lives.
5. The game provides visual feedback on the current state of the word and the remaining lives through Hangman art.

## Example

```plaintext
_______
|     |
|
|
|
|
|________

Guess a letter: a
_ _ a _ _ _

Guess a letter: e
You guessed 'e,' but it's not in the word. You lose a life.
_ _ a _ _ _

_______
|     |
|     O
|     |
|
|
|________

Guess a letter: t
_ _ a t _ _

...

You win!
