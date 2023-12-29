#!/usr/bin/python3

import numpy as np


def read_challenge_text(filepath: str) -> list[list[list[str]]]:
    """
    Parse and load the minefield challenge text and return a list of strings
    that represent each minefield in the file.
    """

    lines = open(filepath, "r").read().splitlines()

    # Parse the raw data into an array of string reps of the minefields
    str_minefields = []
    tmp_mine = []

    for rw_line in lines:
        # A new minefield is starting
        if " " in rw_line:
            if tmp_mine:
                str_minefields.append(tmp_mine.copy())
                tmp_mine = []
            continue

        # '0 0' means that no more data should be read
        if rw_line == "0 0":
            break

        # Parse the line into individual chars in a list
        tmp_mine.append([char for char in rw_line])

    return str_minefields


def parse_minefield(minefield: list[list[str]]) -> np.array:
    """
    Convert a representation of a minefield to a numpy boolean array.
    """
    pass


def mine_count(mines: np.array) -> str:
    """
    Determine the number of adjacent mines for each empty square and produce an
    string representation of the minefield with that infomation.
    """
    pass


if __name__ == "__main__":
    # String representations of the minefields
    raw_minefields = read_challenge_text("./data/sample0.txt")

    print(raw_minefields)
