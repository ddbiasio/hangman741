import random

def select_word() -> str:
    """
    select_word Selects a word froma list

    Returns
    -------
    str
        The selected word
    """
    # List of 5 fruits
    word_list = ["banana", "apple", "watermelon", "grapes", "strawberries"]
    print(word_list)

    # Pick a word at random
    word = random.choice(word_list)
    print(word)

    # retunr the selected word
    return word

def ask_for_input() -> str:
    """
    ask_for_input Prompts user to enter a guess (single letter)
    and validates this to be a single letter

    Returns
    -------
    str
        The user's input
    """
    # Loop until a valid letter is entered
    while True:

        guess = input("Enter a letter you think is in the word: ")

        # Check the input is 1 letter
        
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Oops! That is not a valid input")

    
def check_guess(guess: str, word: str):
    """
    check_guess checks is a letter in the word

    Parameters
    ----------
    guess : str
        A single letter guess
    word : str
        The word being checked for 'guess'
    Returns
    -------
    None
       Nothing is returned
    """
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False
    
if __name__ == "__main__":

    word = select_word()

    guess = ask_for_input()

    check_guess(guess, word)



