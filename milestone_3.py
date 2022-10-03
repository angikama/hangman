# %%
import random
import string

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = ["mango", "pineapple", "grapes", "cherry","banana"]
        self.num_lives = num_lives
        self.word = (random.choice(self.word_list))
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        pass

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:  
            print(f"Good guess! {guess} is in the word.")
            for x, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[x] = letter
                    print(self.word_guessed)

            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess) 


    def ask_for_input(self):
        while True:
            guess = input("Guess a single letter ")
            if (len(guess) > 1) or (guess.isdigit()):
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)
            break

def play_game():
    word_list = ["mango", "pineapple", "grapes", "cherry","banana"]
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives <= 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            game.num_lives > 0 and game.num_letters == 0
            print("Congratulations! You have won the game!")
            break
        
    
        

play_game()

# %%
