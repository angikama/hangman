# %% Importing module
import random

# %% Create a list of favorite fruits and assign to variable
word_list = ["mango", "pineapple", "grapes", "cherry","banana"]

# %% Assigning randomly generated word to variable
word = (random.choice(word_list))

print(word)

guess = input("Enter a single letter")

# %% Checking input is single character
if ((guess >= 'a' and guess <='z') or (guess >= 'A' and guess<='Z')):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
# %%
