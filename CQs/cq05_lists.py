"""Mutating functions."""

__author__ = "730734418"


def manual_append(list: list[int], value: int) -> None:
    """Mutates input by appending int to list[int]"""
    list.append(value)


def double(double_nums: list[int]) -> None:
    """Mutates input by multiplying list elements by 2"""
    index: int = 0
    while index < len(double_nums):
        double_nums[index] = double_nums[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
