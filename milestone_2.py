import random

def select_word() -> str:
    # List of 5 fruits
    word_list = ["banana", "apple", "watermelon", "grapes", "strawberries"]
    print(word_list)

    # Pick a word at random
    word = random.choice(word_list)
    print(word)

    # retunr the selected word
    return word

def get_user_letter() -> str:
# Get a letter from the user
    return input("Enter a letter you think is in the word: ")
    print(guess)

def is_input_valid(guess: str) -> bool:
    # Check the input is 1 letter
    if len(guess) == 1 and guess.isalpha():
        print("Good Guess")
        return True
    else:
        print("Oops! That is not a valid input")
        return False
    
if __name__ == "__main__":
    
    word = select_word()
    guess = get_user_letter()
    if is_input_valid(guess):
        # check the letter
        pass