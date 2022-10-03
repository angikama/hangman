# %%
import random
from turtle import position

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = "mango", "pineapple", "grapes", "cherry","banana"
        self.num_lives = num_lives
        self.word = (random.choice(word_list))
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        pass


    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:  
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess: #Unsure of how to replace the corresponding "_" in the word_guessed with the guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry,{self.guess} is not in the word.")
            print(f"You have{self.num_lives} lives left.") 
    self.list_of_guesses.append(guess) 


    def ask_for_input():
        while True:
            guess = input("Guess a single letter")
            if (len(guess) > 1) or (guess.isdigit()):
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)

def play_game():
    word_list = ["mango", "pineapple", "grapes", "cherry","banana"]
    game = Hangman(word_list, num_lives=5) #should I make lives equal something or not
    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0:
            game.ask_for_input()
        else: #else or elif
            game.num_lives > 0 and game.num_letters == 0
            print("Congratulations! You have won the game!")

# %%
