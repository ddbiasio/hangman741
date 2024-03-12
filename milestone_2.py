import random

# List of 5 fruits
word_list = ["banana", "apple", "watermelon", "grapes", "strawberries"]
print(word_list)
word = random.choice(word_list)
print(word)

guess = input("Enter a letter you think is in the word: ")
print(guess)
