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


if __name__ == "__main__":
    generate_outputs("data/", 3, 3)
