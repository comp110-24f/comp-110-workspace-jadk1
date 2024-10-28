"""Dictionary Utility Functions"""

__author__ = "730734418"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    invert_dict: dict[str, str] = {}
    # Empty dict stores the invetred key-value pairs
    for key in input_dict:
        value = input_dict[key]
        if value in invert_dict:
            # Checks if the value(new key) already exists
            raise KeyError("Duplicate keys not allowed")
        invert_dict[value] = key
        # Switches the keys and values
    return invert_dict


def favorite_color(colors: dict[str, str]) -> str:
    count: dict[str, int] = {}
    # Create empty dict to store color counts
    for name in colors:
        color = colors[name]
        # Populate dict with each name's associated color
        if color in count:
            # Add to count if color exists, or add to dict
            count[color] += 1
        else:
            count[color] = 1
    max: int = -1
    favorite: str = ""
    # Max count and favorite color variables
    for name in colors:
        color = colors[name]
        if count[color] > max:
            # If color count is higher than current max,
            # Set color as new favorite
            max = count[color]
            favorite = color
        elif count[color] == max and favorite == "":
            favorite = color
        # If there's a tie, the first color remains the favorite
    return favorite


def count(item_list: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    # Empty dict stores counts of each item
    for elem in item_list:
        if elem in count_dict:
            # Increase count if item exists, or set to 1 if first occurance
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    return count_dict


def alphabetizer(input_words: list[str]) -> dict[str, list[str]]:
    alphabetized_words: dict[str, list[str]] = {}
    # Empty dict to store list of words
    for elem in input_words:
        first_letter: str = elem[0].lower()
        # Converts first letter to lowercase
        if first_letter not in alphabetized_words:
            # If letter isn't in dict start an empty list
            alphabetized_words[first_letter] = []
        alphabetized_words[first_letter].append(elem)
        # Adds the word to the list of alphabetized words
    return alphabetized_words


def update_attendance(att: dict[str, list[str]], day: str, student: str) -> None:
    if day in att:
        # Checks if the day already exists
        if student not in att[day]:
            att[day].append(student)
        # Only adds student if they aren't already present
    else:
        att[day] = [student]
    # If the day isn't in dict, initialize with a list containing student's name
