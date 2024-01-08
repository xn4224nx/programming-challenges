#!/usr/bin/python3
"""
GENERATE CHALLENGE SAMPLES
==========================

Generate text in files that simulates valid inputs to the contest. The script 
will also create the valid answers to the challenge.

Each line in the input file starts with with the size of the display size. It is
then followed by the digits that need to be displayed.
"""

import random
from pathlib import Path


MAX_PRINT_NUM = 99999999
MAX_SIZE = 10


def generate_outputs(outdir: str, num_files: int, num_per_file: int):
    """
    Create `num_file` of output files that are inputs to the challenge.
    """

    base_dir = Path(outdir)
    base_dir.mkdir(parents=True, exist_ok=True)

    for file_num in range(num_files):
        outfile = Path(base_dir, f"comp_input_{file_num:02}.txt")

        with outfile.open("a") as fp:
            for _ in range(num_per_file):
                size = random.randint(1, MAX_SIZE)
                print_n = random.randint(0, MAX_PRINT_NUM)

                fp.write(f"{size} {print_n}\n")


def large_print_int(num: int, size: int) -> str:
    """
    Create a string representation of an integer number.
    """
    
    if size <= 0 or size > MAX_SIZE:
        raise Exception(f"Unsupported size: {size}")
    
    elif num < 0 or num > MAX_PRINT_NUM:
        raise Exception(f"Number cannot be printed: {num}")
    
    num = str(num)

    top = ""
    mid1 = [""] * size
    half = ""
    mid2 = [""] * size
    low = ""

    for char in num:
        # Create the top string
        if char in ["1", "4"]:
            top += (size+2) * " "
        else:
            top += " " + "-" * size + " "

        # Create the first middle string
        for i in range(len(mid1)):
            if char in ["1", "2", "3", "7"]:
                mid1[i] += " " + size * " " + "|"
            elif char in ["5", "6"]:
                mid1[i] += "|" + size * " " + " "
            else:
                mid1[i] += "|" + size * " " + "|"

        # Create the half way string
        if char in ["1", "7", "0"]:
            half += (size+2) * " "
        else:
            half += " " + size * "-" + " "

        # Create the second middle string
        for j in range(len(mid2)):
            if char in ["0", "8", "6"]:
                mid2[j] += "|" + size * " " + "|"
            elif char in ["2"]:
                mid2[j] += "|" + size * " " + " "
            else:
                mid2[j] += " " + size * " " + "|"

        # Create the bottom string
        if char in ["1", "4", "7"]:
            low += (size+2) * " "
        else:
            low += " " + size * "-" + " "

        # Add the space between numbers
        top += "  "
        mid1 = [x + "  " for x in mid1]
        half += "  "
        mid2 = [x + "  " for x in mid2]
        low += "  "

    # Finish off the strings with a new line
    top += "\n"
    mid1 = [x + "\n" for x in mid1]
    half += "\n"
    mid2 = [x + "\n" for x in mid2]
    low += "\n"

    # Combine all the strings
    return top + "".join(mid1) + half + "".join(mid2) + low


if __name__ == "__main__":
    generate_outputs("data/", 3, 3)
    print(large_print_int(1234567890, 5))
