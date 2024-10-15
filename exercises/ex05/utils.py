"""List Utility Functions"""

__author__ = "730734418"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list containing only even integers"""
    output = []  # create empty list to track evens
    for int in input:  # for loop to iterate through list
        if int % 2 == 0:  # Use modulo to check if even
            output.append(int)  # Add evens to empty list
    return output


def sub(input: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Return a subset of input list from start index to end index"""
    output = []  # Create empty tracker list
    if len(input) == 0 or start_idx >= len(input) or end_idx <= 0:
        # Arguments that should result in an empty list
        return output

    if start_idx < 0:
        start_idx = 0
    # If start index is negative, start from beginning of list
    if end_idx > len(input):
        end_idx = len(input)
    # If end index is greater than length of list, end with end of list

    for idx in range(start_idx, end_idx):
        output.append(input[idx])
    # Use for loop to iterate through elements in the range and add to tracker list
    return output


def add_at_index(input: list[int], elem: int, idx: int) -> None:
    """Inserts element at specified index in input list"""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # Placeholder at end of list to make space for input
    for i in range(len(input) - 1, idx, -1):
        input[i] = input[i - 1]
    # Shifts elements of list to the right starting from the end to the index position
    input[idx] = elem
    # Places new element at idx
