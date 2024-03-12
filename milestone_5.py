import random
class Hangman:
    """
    This class implements the game of Hangman

    Attributes
    ----------
    word : str
        The word being guessed
    word_guessed : list
        A list of characters that have been guessed
    num_letters : int
        The number of UNIQUE letters in the word that have not been guessed
    num_lives : int
        The number of lives the player has at the start of the game
    word_list : list
        A list of words
    list_of_guesses : list
        A list of the guesses that have already been tried

    Methods
    -------
    check_guess(guess: str) -> None
        Accepts a single letter and checks is it in the word
    ask_for_input() -> None
        Gets input from use, validates and passes it to check_guess
    """

    def __init__(self, word_list: list, num_lives: int) -> None:
        """
        __init__ Initialises the Hangman game

        Parameters
        ----------
        word_list : list
            List of words to select a random word from
        num_lives : int
            Number of lives to allow the user to guess the word
        """
        self.word = random.choice(word_list).lower()
        self.word_list = word_list
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess: str):
        """
        check_guess checks is a letter in the word

        Parameters
        ----------
        guess : str
            A single letter guess
        Returns
        -------
        None
        Nothing is returned
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word")

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            
            self.num_letters -= 1

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        ask_for_input Prompts user to enter a guess (single letter)
        and validates this to be a single letter

        Returns
        -------
        None
        """
        # Loop until a valid letter is entered
        # When a valid letter is found check if it is in the word

        while True:

            guess = input("Enter a letter you think is in the word: ")

            # Check the input is 1 letter
            
            if not(len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list: list):
    """
    play_game Instantiates the Hangman object and plays the game

    Parameters
    ----------
    word_list : list
        A list of unique words to guess from
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    # Loop while the user has lives left and there are still letters to guess
    while True:
        if game.num_lives == 0:
            print("You lost! The word was {game.word}.")
            break
        elif game.num_letters > 0:
            guess = game.ask_for_input()
        else:
            print(f"Congratulations. You won the game! The word was {game.word}.")
            break

if __name__ == "__main__":

    # create a word list
    word_list = ["banana", "apple", "watermelon", "grapes", "strawberries"]

    # play the game using your word list
    play_game(word_list)
