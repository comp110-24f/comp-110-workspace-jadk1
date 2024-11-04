"""File to define Fish class."""

__author__ = "730734418"


class Fish:
    """Class for fish in river."""

    def __init__(self):
        """Constructor for Fish class."""
        self.age = 0
        return None

    def one_day(self):
        """Simulate one day for a Fish by increasing age."""
        self.age += 1
        return None
