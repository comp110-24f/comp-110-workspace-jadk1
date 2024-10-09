"""Conditionals/Variables/Input CQ"""

__author__ = "730734418"


def guess_a_number() -> None:
    """Takes a user guess and checks if it matches the secret number"""
    secret: int = 7  # Variable Definition
    x: str = input("Guess a number:")  # X is local variable
    print("Your guess was " + str(x))
    if int(x) == 7:
        print("You got it!")
    elif int(x) < 7:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
