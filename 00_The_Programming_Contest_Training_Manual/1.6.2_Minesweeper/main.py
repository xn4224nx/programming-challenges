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
    tmp_mine = np.array(minefield)
    bool_mine = np.where(tmp_mine == "*", True, False)

    return bool_mine


def mine_count(mines: np.array) -> str:
    """
    Determine the number of adjacent mines for each empty square and produce an
    string representation of the minefield with that infomation.
    """

    tmp_mine = ""

    for i in range(mines.shape[0]):
        for j in range(mines.shape[1]):
            # Leave mines as none
            if mines[i][j]:
                tmp_mine += "*"
                continue

            # Otherwise count the number of adjacent mines
            adj_mines = 0

            if i == 0:
                if j == 0:
                    adj_mines += mines[i][j + 1]
                    adj_mines += mines[i + 1][j + 1]
                    adj_mines += mines[i + 1][j]

                elif j == mines.shape[1] - 1:
                    adj_mines += mines[i][j - 1]
                    adj_mines += mines[i + 1][j - 1]
                    adj_mines += mines[i + 1][j]

                else:
                    adj_mines += mines[i][j - 1]
                    adj_mines += mines[i][j + 1]
                    adj_mines += mines[i + 1][j - 1]
                    adj_mines += mines[i + 1][j + 1]
                    adj_mines += mines[i + 1][j]

            elif i == mines.shape[0] - 1:
                if j == 0:
                    adj_mines += mines[i - 1][j]
                    adj_mines += mines[i - 1][j + 1]
                    adj_mines += mines[i][j + 1]

                elif j == mines.shape[1] - 1:
                    adj_mines += mines[i - 1][j - 1]
                    adj_mines += mines[i - 1][j]
                    adj_mines += mines[i][j - 1]

                else:
                    adj_mines += mines[i - 1][j - 1]
                    adj_mines += mines[i - 1][j]
                    adj_mines += mines[i - 1][j + 1]

                    adj_mines += mines[i][j - 1]
                    adj_mines += mines[i][j + 1]

            else:
                if j == 0:
                    adj_mines += mines[i - 1][j]
                    adj_mines += mines[i - 1][j + 1]
                    adj_mines += mines[i][j + 1]
                    adj_mines += mines[i + 1][j + 1]
                    adj_mines += mines[i + 1][j]

                elif j == mines.shape[1] - 1:
                    adj_mines += mines[i - 1][j - 1]
                    adj_mines += mines[i - 1][j]
                    adj_mines += mines[i][j - 1]
                    adj_mines += mines[i + 1][j - 1]
                    adj_mines += mines[i + 1][j]

                else:
                    adj_mines += mines[i - 1][j - 1]
                    adj_mines += mines[i - 1][j]
                    adj_mines += mines[i - 1][j + 1]

                    adj_mines += mines[i][j - 1]
                    adj_mines += mines[i][j + 1]

                    adj_mines += mines[i + 1][j - 1]
                    adj_mines += mines[i + 1][j + 1]
                    adj_mines += mines[i + 1][j]

            tmp_mine += str(adj_mines)
        tmp_mine += "\n"
    return tmp_mine


if __name__ == "__main__":
    # String representations of the minefields
    raw_minefields = read_challenge_text("./data/sample0.txt")

    # Convert to numpy array of bools
    mine_bool = parse_minefield(raw_minefields[0])

    # Count the number of adjacent mines
    count_map = mine_count(mine_bool)
