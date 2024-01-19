def simple_guess_game():
  #Guess Game
  print("Welcome to the Computer Guessing Game!")
  target_number = int(input("Choose a number for the computer to guess: "))

  low = 1
  high = 100
  computer_guess = 0

  while True:
    computer_guess = (low + high) // 2

    print(f"Computer guesses: {computer_guess}")

    if computer_guess == target_number:
      print("Computer guessed the correct number!")
      break
    elif computer_guess < target_number:
      print("Too low. Computer will guess higher.")
      low = computer_guess + 1
    else:
      print("Too high. Computer will guess lower.")
      high = computer_guess - 1
