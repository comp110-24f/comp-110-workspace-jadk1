"""While Loops CQ"""

__author__ = "730734418"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    print(count)
