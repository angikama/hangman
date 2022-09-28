# %% Importing module
import random

# %% Create a list of favorite fruits and assign to variable
word_list = ["mango", "pineapple", "grapes", "cherry","banana"]

# %% Assigning randomly generated word to variable
word = (random.choice(word_list))

print(word)

guess = input("Enter a single letter")

# %% Checking input is single alphabetic character
if (len(guess) <= 1) and (guess.isalpha()):
        print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# %%
