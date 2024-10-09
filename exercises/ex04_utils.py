"""List Utils Exercise"""

__author__ = "730734418"


def all(list_checked: list[int], num_checked: int) -> bool:
    """Checks whether or not all ints in the list are the same as the given int"""
    if len(list_checked) == 0:
        # Checks if list is empty
        return False
    while len(list_checked) > 0:
        elem = list_checked.pop()
        # Iterates through list by removing elements from end
        if elem != num_checked:
            # If number doesn't match the parameter, return False
            return False
    return True
    # If all conditions are met, return True


def max(max_list: list[int]) -> int:
    """Returns highest value of a list"""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    largest = max_list.pop()
    # Assumne first element removed is largest initally
    while len(max_list) > 0:
        # Check remaining elements to see if they're larger
        # Replace largest if any elements are larger
        current = max_list.pop()
        if current > largest:
            largest = current
    return largest


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if every element at every index is equal"""
    if len(list_1) != len(list_2):
        # Checks if lengths of lists are equal
        return False
    while len(list_1) > 0:
        # Iterates through elements by popping them from each list
        if list_1.pop() != list_2.pop():
            # Compares the last element of each list
            return False
    return True
    # If all elements match up, return True


def extend(original_list: list[int], append_list: list[int]) -> None:
    """Appends second list's values to the end of the first"""
    temp_list = []
    # Temporary list stores elements in original order s
    # Since using pop reverses order
    while len(append_list) > 0:
        temp_list.append(append_list.pop())
    # Used pop to remove elements form end of append_list
    # And append them to the temporary list
    while len(temp_list) > 0:
        original_list.append(temp_list.pop())
    # Appends elements from temporary list to the original list
    # In the correct order
