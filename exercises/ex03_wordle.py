"""Wordle Exercise"""

__author__ = "730734418"


def input_guess(word_length: int) -> str:
    """Takes an input word and checks if it's the correct length"""
    guess = input(f"Enter a {word_length} character word: ")
    # f string allows word_length parameter to be included in string for guess variable
    while len(guess) != word_length:
        # Means while the length of the guess does not equal the length of the word
        guess = input(f"That wasn't {word_length} chars! Try again: ")
    return guess


def contains_char(word: str, char: str) -> bool:
    """Checks if character matches any index in word"""
    assert len(char) == 1
    index = 0  # Define index variable to keep track of indices
    while index < len(word):  # Typical while loop to circle through indices in a word
        if word[index] == char:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"  # Define globals for emojified function
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(user_guess: str, secret_word: str) -> str:
    """Compares user guess with secret word and returns emoji string"""
    """Green box for correct letter in correct position"""
    """Yellow box for correct letter in wrong position"""
    """White box for incorrect letter"""
    assert len(user_guess) == len(secret_word)
    emoji_string: str = ""  # Build on an empty string to form the completed string
    index: int = 0  # Create another index variable to keep track of indices
    while index < len(user_guess):
        # Another while loop is used to cycle through indices
        if user_guess[index] == secret_word[index]:
            # If the indices on the guess and the word match
            emoji_string += GREEN_BOX  # Add a green box onto the empty emoji string
        elif contains_char(secret_word, user_guess[index]):
            # Uses the contains_char function to check if the character is in the word
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        index += 1
    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    # This variable keeps track of each turn
    max_turns: int = 6
    # This variable sets the max number of turns to 6
    winner: bool = False
    # This variable defines when the player wins and the code stops

    while turns <= max_turns and not winner:
        # While the number of turns is less than 6 and the player hasn't won
        print(f"=== Turn {turns}/{max_turns} ===")
        # f string used to insert turn number inside the string
        guess = input_guess(len(secret))
        # New guess variable takes the guess that is checked by the input_guess function
        turn_check = emojified(guess, secret)
        # turn_check variable prints the emoji string from emojified
        # using the new guess variable and secret word as arguments
        print(turn_check)
        if guess == secret:
            # This if statement checks if the player has guessed the right word
            winner = True
        else:
            turns += 1

    if winner:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
