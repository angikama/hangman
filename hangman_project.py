# %%
import random
import string


class Hangman():
    '''
    This class is used to represent the Hangman game

    Attributes:
        num_lives (int): the set number of lives the user has

    Methods:
        __init__ (self, num_lives=5)

    '''
    
    def __init__(self, word_list, num_lives=5):
        '''
        Class constructor to initialise attributes of the class

        '''
        self.word_list = ["mango", "apple", "grape", "guava", "peach", "kiwi", "lemon"]
        self.num_lives = num_lives
        self.word = (random.choice(self.word_list))
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
 
# %%
    def hangman_display(self):
        '''
        This function displays the hangman visual

        '''
        if self.num_lives == 4:
            print ("_________")
            print ("|    |")
            print ("|    O")
            print ("|    |")
            print ("|    |")
            print ("|")
            print ("|________")
        elif self.num_lives == 3:
            print ("_________")
            print ("|    |")
            print ("|    O")
            print ("|   \|")
            print ("|    |")
            print ("|")
            print ("|________")
        elif self.num_lives == 2:
            print ("_________")
            print ("|    |")
            print ("|    O")
            print ("|   \|/")
            print ("|    |")
            print ("|")
            print ("|________")
        elif self.num_lives == 1:
            print ("_________")
            print ("|    |")
            print ("|    O")
            print ("|   \|/")
            print ("|    |")
            print ("|   /")
            print ("|________")
        elif self.num_lives == 0:
            print ("_________")
            print ("|    |")
            print ("|    O")
            print ("|   \|/")
            print ("|    |")
            print ("|   / \ ")
            print ("|________")
        return
# %%
    def check_guess(self, guess):
        '''
        This function checks the if the user's guess is in the chosen random word

        Parameters:
            guess: single alphabetical character input from the user

        '''
        guess = guess.lower()
        if guess in self.word:  
            print(f"Good guess! {guess} is in the word.")
            print(f'You have {self.num_lives} lives left')
            for x, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[x] = letter
                    print(self.word_guessed)  
                if self.word_guessed.count('_') <= 0:
                    print("Congratulations! You have won the game!")
                    break
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            self.hangman_display()
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess) 


    def ask_for_input(self):
        '''
        This function asks the user for input and checks whether it is a unique single, alphabetical character

        '''
        while True:
            guess = input("Welcome to Hangman, Guess a single letter")
            if (len(guess) > 1) or (guess.isdigit()):
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)
            break

def play_game():
    '''
    This function runs all the code that allows the game to be played 

    '''
    word_list = ["mango", "apple", "grape", "guava", "peach", "kiwi", "lemon"]
    game = Hangman (word_list, num_lives=5)
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
