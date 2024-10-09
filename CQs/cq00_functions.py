"""Functions CQ"""

__author__ = "730734418"


# Mimic Function
def mimic(message: str) -> str:
    """Mimics message"""
    return message


# Main Function
def main() -> None:
    """Prints result of calling mimic function"""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()
