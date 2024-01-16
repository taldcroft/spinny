import itertools
import sys

import numpy as np
import numba

NN = 0  # No number

# The wheels are represented as a 5 x 4 x 12 array, where each 4x12 array is a wheel.
# The wheels are defined in order from top to bottom. For a given row and column on the
# toy, search through the wheels in order until a nonzero value is found.
#
# Wheel rotation to a different hour angle is accomplished by adding an offset to the
# column index and taking mod 12. The offset is the number of hours to rotate
# counterclockwise.
WHEELS = [
    [
        [NN, 10, NN, 7, NN, 15, NN, 8, NN, 3, NN, 6],
        [NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN],
        [NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN],
        [NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN],
    ],
    [
        [7, 3, NN, 6, NN, 11, 11, 6, 11, NN, 6, 17],
        [4, NN, 7, 15, NN, NN, 14, NN, 9, NN, 12, NN],
        [NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN],
        [NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN],
    ],
    [
        [4, 5, NN, 7, 8, 9, 13, 9, 7, 13, 21, 17],
        [26, 14, 1, 12, NN, 21, 6, 15, 4, 9, 18, 11],
        [NN, 16, NN, 9, NN, 5, NN, 10, NN, 8, NN, 22],
        [NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN, NN],
    ],
    [
        [NN, 16, 2, 7, NN, 9, NN, 7, 14, 11, NN, 8],
        [8, 9, NN, 9, 20, 12, 3, 6, NN, 14, 12, 3],
        [19, 3, 12, 3, 26, 6, NN, 2, 13, 9, NN, 17],
        [NN, 10, NN, 1, NN, 9, NN, 12, NN, 6, NN, 10],
    ],
    [
        [11, 14, 11, 11, 14, 11, 14, 11, 14, 14, 11, 14],
        [14, 15, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [9, 9, 4, 4, 6, 6, 3, 3, 14, 14, 21, 21],
        [7, 8, 8, 3, 4, 12, 2, 5, 10, 7, 16, 8],
    ],
]

# Numba does not support multidimensional lists, so convert to numpy array. For pure
# Python a list of lists is faster.
WHEELS = np.array(WHEELS)


@numba.njit(cache=True)
def spin_and_check(offsets, wheels):
    """Loop through columns and rows and check that the sum of each column is 42.

    Loop first through columns, then rows, then wheels. If the sum for a given column
    is not 42, then the offset is not a solution.
    """
    for col0 in range(12):
        sum = 0
        for row in range(4):
            for offset, wheel in zip(offsets, wheels):
                col = (col0 + offset) % 12
                val = wheel[row][col]
                if val != NN:
                    sum += val
                    break

        if sum != 42:
            return False

    return True


def get_visible_wheel(offsets: list[int]):
    """Print the wheel that is visible from the top"""
    visible_wheel = np.zeros((4, 12), dtype=np.uint8)
    for col0 in range(12):
        for row in range(4):
            for offset, wheel in zip(offsets, WHEELS):
                col = (col0 + offset) % 12
                if (val := wheel[row][col]) != NN:
                    visible_wheel[row][col0] = val
                    break
            else:
                raise ValueError("no visible wheel")
    return visible_wheel


def find_meaning_of_life(wheels):
    """Brute-force spin the wheels until the answer is found"""
    # Equivalent to a 4-deep nested for loop
    offsets_iter = itertools.product(range(12), repeat=len(wheels) - 1)
    for ii, offsets4 in enumerate(offsets_iter):
        offsets = offsets4 + (0,)
        if spin_and_check(offsets, wheels):
            return ii, offsets


def main():
    iter = int(sys.argv[1])
    for _ in range(iter):
        n_iter, offsets = find_meaning_of_life(WHEELS)

    print(f"Found solution in {n_iter} iterations")
    print(f"offsets = {offsets} (drag counterclockwise)")
    print("Visible wheel")
    vw = get_visible_wheel(offsets)
    print(vw)
    print()
    print("Sum of each column")
    print(np.sum(vw, axis=0))


if __name__ == "__main__":
    main()
