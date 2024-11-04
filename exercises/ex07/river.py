"""File to define River class."""

__author__ = "730734418"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class for river simulation."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove Fish older than 3 days and Bears older than 5."""
        new_bear_list: list[Bear] = []  # new list for bears
        for bear in self.bears:
            if bear.age <= 5:
                new_bear_list.append(bear)
                # Loop through bears and add to list if bear is younger than 5
        self.bears = new_bear_list
        new_fish_list: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish_list.append(fish)  # Same as bear method
        self.fish = new_fish_list
        return None

    def remove_fish(self, amount: int):
        """Remove amnt of fish from front of fish list."""
        self.fish = self.fish[amount:]  # Removes first amount fish

    def bears_eating(self):
        """Each bear eats 3 fish if >= 5 fish in river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # Remove 3 fish from river
                bear.eat(3)  # Increase bear hunger_score
        return None

    def check_hunger(self):
        """Remove bears with hunger score < 0."""
        alive_bears: list[Bear] = []
        # New list for bears with hunger score >= 0
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        # Update original bears list
        return None

    def repopulate_fish(self):
        """Add new fish to river for each fish pair."""
        new_fish = (len(self.fish) // 2) * 4
        # Number of new fish for each pair
        self.fish += [Fish()] * new_fish
        return None

    def repopulate_bears(self):
        """Add new bears to river for each bear pair."""
        new_bears = len(self.bears) // 2
        # Number of new bears based on pairs
        self.bears += [Bear()] * new_bears
        # Create list of new Bear instances and add it to existing list
        return None

    def view_river(self):
        """Display current state of river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
