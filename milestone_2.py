import random

# List of 5 fruits
word_list = ["banana", "apple", "watermelon", "grapes", "strawberries"]
print(word_list)

# Pick a word at random
word = random.choice(word_list)
print(word)

# Get a letter from the user
guess = input("Enter a letter you think is in the word: ")
print(guess)

# Check the input is 1 letter
if len(guess) == 1 and guess.isalpha():
    print("Good Guess")
else:
    print("Oops! That is not a valid input")