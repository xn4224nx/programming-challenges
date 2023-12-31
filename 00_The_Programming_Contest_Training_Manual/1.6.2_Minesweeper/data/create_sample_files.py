#!/usr/bin/python3

import numpy as np
import random


def create_minefield(size: [int, int], mine_prob: float) -> np.array:
    """
    Create a rectangular minefield of dimensions of 'size', clear patches are
    '.' and mines are '*'. The probability of a space containing a mine is
    'mine_prob'.
    """

    # Generate an array of probability
    prob_arr = np.random.rand(size[1], size[0])

    # Create an array of strings
    mine_arr = np.where(prob_arr > mine_prob, ".", "*")

    return mine_arr


def create_sample_file(num_fields: int, file_path: str):
    """
    Fill a file with a number of minefields in the format required for the
    problem.
    """

    file_cont = ""

    for _ in range(num_fields):
        # Generate the features of the minefield
        height = random.randint(3, 100)
        width = random.randint(3, 100)
        prob_of_mine = random.betavariate(2, 8)

        # Create the minefield
        minef = create_minefield((height, width), prob_of_mine)

        # Add the minefield header
        file_cont += f"{width} {height}\n"

        # Add the minefield
        for i in range(minef.shape[0]):
            for j in range(minef.shape[1]):
                file_cont += minef[i][j]
            file_cont += "\n"

    # Add the final line
    file_cont += "0 0\n"

    # Save the string to a text file
    with open(file_path, "w") as text_file:
        print(file_cont, file=text_file)


if __name__ == "__main__":
    create_sample_file(20, "mine0.txt")
    create_sample_file(10, "mine1.txt")
    create_sample_file(2, "mine2.txt")
    create_sample_file(7, "mine3.txt")
    create_sample_file(100, "mine4.txt")
