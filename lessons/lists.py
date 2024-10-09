"""Basic syntax of lists"""

# Empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # contructor

# Add to list
my_numbers.append(1.5)
my_numbers.append(2.3)

# Creating an already populated list
game_points: list[int] = [102, 86, 94]

# Indexing
game_points[2]
last_game: int = game_points[2]

# Modifying by index
# Lists are mutable
game_points[1] = 72

# Length of list
len(game_points)

# Remove item from list
game_points.pop(1)


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""
    idx: int = 0
    while idx < len(int_list):
        print(int_list[idx])
        idx += 1


display(int_list=game_points)
