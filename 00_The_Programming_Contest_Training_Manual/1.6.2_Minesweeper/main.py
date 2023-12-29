#!/usr/bin/python3

import numpy as np


def read_challenge_text(filepath: str) -> list[str]:
    """
    Parse and load the minefield challenge text and return a list of strings
    that represent each minefield in the file.
    """

    lines = open(filepath, "r").readlines()

    # Parse the raw data into an array of string reps of the minefields
    str_minefields = []
    tmp_mine = ""

    for rw_line in lines:
        # '0 0' means that no more data should be read
        if rw_line == "0 0":
            break

        # Otherwise a new minefield is starting
        elif " " in rw_line:
            if tmp_mine != "":
                str_minefields.append(tmp_mine)
                tmp_mine = ""
            continue

        tmp_mine += rw_line

    return str_minefields


def parse_minefield(minefield: str) -> np.array:
    pass


def mine_count(mines: np.array) -> str:
    pass


if __name__ == "__main__":
    # String representations of the minefields
    raw_minefields = read_challenge_text("./data/sample0.txt")
