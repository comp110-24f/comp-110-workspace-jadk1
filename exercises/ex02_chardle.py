"""Chardle Exercise"""

__author__ = "730734418"


def input_word() -> str:
    """Takes input word and checks if 5 characters"""
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) == 5:
        # Used len function to check input word
        return user_word
    else:
        print("Error: Word must contain 5 characters.")
        # Use print function before return so that it runs
        exit()
        # Use exit function to end program here in else block


def input_letter() -> str:
    """Takes input letter and checks if 1 character"""
    user_char: str = input("Enter a single character: ")
    if len(user_char) == 1:
        # Used len function to check input letter
        return user_char
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """Counts instances of input letter in input word"""
    print("Searching for " + letter + " in " + word)
    # Had to concatenate strings
    count: int = 0
    # count variable tracks instances of letter
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
        # Only add 1 to count each time because
        # if block is skipped if index not found
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
        # After checking indexes, this if statement uses count variable
        # To total the number of instances the letter is found
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
        # Added this to create separate message for 1 instance
        # Had to use elif here instead of if
        # Because this is a separate condition
        # So control flow is changed
    else:
        print((str(count) + " instances of " + letter + " found in " + word))
        # Use else to end the series of if statements


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    # Make sure to add parantheses after each function call


if __name__ == "__main__":
    main()
