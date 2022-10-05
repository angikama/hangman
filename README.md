# Hangman
## Introduction
This code codes for a Hangman game, a random word is chosen from a word list and the user guesses single letters until they guess the full word. The user has 5 lives, with every life lost, the corresponding hangman visual is displayed. 

## Functions
- check_guess
  - Converts the user's input into lowercase
  - Checks whether the user's guess is in the chosen random word
  - Replaces the '_' placeholder with the correct input
  - Decreases number of lives by 1 if there is an inccorect guess and the corresponding hangman display 

- ask_for_input
  - Asks the user to guess a letter using enumerate
  - Checks if the guess is a unique, single alphabetical character
  - Stores the guesses in a list so that the user is informed if they have already guessed a character

- play_game
	- Allows the game to be played
	- A while loop is used to set conditions to end the game depending on whether the user won or lost
