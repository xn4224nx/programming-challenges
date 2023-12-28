#!/usr/bin/python3


def hailstones(start_n: int) -> int:
    """
    Execute one step for the collatz conjecture.
    """
    while True:
        if start_n == 1:
            break

        elif start_n % 2 == 0:
            start_n //= 2

        else:
            start_n = 3 * start_n + 1

        yield start_n


def max_hail_cycle(start_h: int, end_h: int) -> int:
    """
    Find the maximum cycle length of all the starting numbers in the envelope
    defined by 'start_h' and 'end_h'.
    """

    # Record all the cycles seen by the function
    max_cycles = {}
    max_c = 0

    # Test each possible hailstone starting number
    for hail in range(start_h, end_h + 1):
        temp_max = 1

        # Go through each individual hail
        for i in hailstones(hail):
            # Check for cycles that have been seen before
            if i in max_cycles:
                temp_max += max_cycles[i]
                break
            else:
                temp_max += 1

        # Save the result
        max_cycles[hail] = temp_max

        # Set the new maximum
        if temp_max > max_c:
            max_c = temp_max

    return max_c


if __name__ == "__main__":
    assert max_hail_cycle(1, 10) == 20
    assert max_hail_cycle(100, 200) == 125
    assert max_hail_cycle(201, 210) == 89
    assert max_hail_cycle(900, 1000) == 174
