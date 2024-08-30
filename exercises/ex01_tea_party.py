"""Tea Party Exercise"""

__author__ = "730734418"


# Main Planner Function
def main_planner(guests: int) -> None:
    """Entrypoint of program- calls functions and produces each output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Needed to concatenate strings not just insert guests in the string
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # Had to set people = guests and convert tea_bags to string to concatenate
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=(tea_bags(people=guests)), treat_count=(treats(people=guests))
            )
        )
    )
    # Not sure why the code is identing here when I save it, but when I run it it works
    # maybe the line is too long?
    # At first, I assigned new variables but I didn't realize that this wasn't allowed
    # So I reworked it to only use variables already avaiable
    return None


# Teabags Function
def tea_bags(people: int) -> int:
    """Computes number of teabags needed based on guests"""
    return people * 2


# Treats Function
def treats(people: int) -> int:
    """Computes number of treats needed based on teas"""
    # people=people is keyword argument,
    # it passes value of "people" from treats
    # to "people" from tea_bags function
    return int(tea_bags(people=people) * 1.5)


# Cost Function
def cost(tea_count: int, treat_count: int) -> float:
    """Computes total cost of teabags and treats"""
    # Had to remove defined variables here too
    # Need to not overcomplicate things unnecessarily
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
