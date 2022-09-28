# Hangman
## Milestone 1
- This code defines a list of words and chooses a random word from the list, it then asks the user for input and checks whether the input is a single alphabetic character
  - The variable created is called word list, with 5 names of fruits
  - The 'random' module is used to give us a random choice from the list
  - The input from the user must be a single alphabetic character for it to be a good guess, if not the message "Oops! That is not a valid input." is shown
  
## Milestone 3
- Functions are created to ask for and check the user's input
- Function 'check_guess' converts the user's input into lowercase and checks whether the user's guess is in the chosen random word
- Function 'ask_for_input' asks the user to guess a letter and checks if the guess is a single alphabetic character
  - If the guess meets the conditons, the message "Good guess" is printed
  - If the guess does not meet the conditons, the message "Invalid letter. Please, enter a single alphabetical character." is printed
- Function 'check_guess' was called in the 'ask_for_input' function
