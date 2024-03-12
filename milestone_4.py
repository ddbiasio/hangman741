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

            for letter, index in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            
            self.num_letters -= 1

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self) -> str:
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
            
            if not(len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)