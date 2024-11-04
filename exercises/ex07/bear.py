"""File to define Bear class."""

__author__ = "730734418"


class Bear:
    """Class for bears in river."""

    def __init__(self):
        """Constructor for Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulate one day for a Bear by increasing age."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Updates Bear hunger_score based on number of fish eaten."""
        self.hunger_score += num_fish
