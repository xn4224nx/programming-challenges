#!/usr/bin/python3
"""
GENERATE CHALLENGE SAMPLES
==========================

Generate text in files that simulates valid inputs to the contest. The script 
will also create the valid answers to the challenge.

Each trip starts with a single line indicating the number of students, this is 
then followed by the amount paid by each student as a two decimal point number.
The file will end with a zero.
"""

import random
import numpy as np

MAX_STUDENTS = 1000
MAX_SPEND_CENTS = 1000000


def gen_chal(que_file: str, ans_file: str, num_trips: int):
    """
    Generate the question and answer text files.
    """

    rng = np.random.default_rng()

    # Fill the files iteratively
    for _ in range(num_trips):
        # Generate the student spend ammounts
        num_students = int(rng.integers(low=1, high=MAX_STUDENTS + 1, size=1)[0])
        amount_spent = rng.integers(low=0, high=MAX_SPEND_CENTS, size=num_students)

        # Output the question
        with open(que_file, "a") as qfp:
            qfp.write(f"{num_students}\n")
            for num in amount_spent:
                qfp.write(f"{num/100 :.02f}\n")

        # Generate the minimum exchange amount
        avg = np.round(np.mean(amount_spent))
        pos_dif = np.sum(amount_spent[amount_spent > avg] - avg)
        neg_dif = np.sum(avg - amount_spent[amount_spent <= avg])
        exchange = int(min(pos_dif, neg_dif))

        # Output the answers
        with open(ans_file, "a") as afp:
            afp.write(f"£{exchange/100 :.02f}\n")

    # Finish Off the question file
    with open(que_file, "a") as qfp:
        qfp.write("0\n")


if __name__ == "__main__":
    for i in range(3):
        gen_chal(f"./data/ques_{i:02}.txt", f"./data/answ_{i:02}.txt", 5)
