"""Coordinates CQ04"""

__author__ = "730734418"


def get_coords(xs: str, ys: str) -> None:
    index_1 = 0
    while index_1 < len(xs):
        index_2 = 0
        while index_2 < len(ys):
            print(f"{xs[index_1]},{ys[index_2]}")
            index_2 += 1
        index_1 += 1
