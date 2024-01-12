import itertools

import numpy as np
import numba

nn = 0  # No number

wheels = [
    [
        [nn, 10, nn, 7, nn, 15, nn, 8, nn, 3, nn, 6],
        [nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn],
        [nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn],
        [nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn],
    ],
    [
        [7, 3, nn, 6, nn, 11, 11, 6, 11, nn, 6, 17],
        [4, nn, 7, 15, nn, nn, 14, nn, 9, nn, 12, nn],
        [nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn],
        [nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn],
    ],
    [
        [4, 5, nn, 7, 8, 9, 13, 9, 7, 13, 21, 17],
        [26, 14, 1, 12, nn, 21, 6, 15, 4, 9, 18, 11],
        [nn, 16, nn, 9, nn, 5, nn, 10, nn, 8, nn, 22],
        [nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn, nn],
    ],
    [
        [nn, 16, 2, 7, nn, 9, nn, 7, 14, 11, nn, 8],
        [8, 9, nn, 9, 20, 12, 3, 6, nn, 14, 12, 3],
        [19, 3, 12, 3, 26, 6, nn, 2, 13, 9, nn, 17],
        [nn, 10, nn, 1, nn, 9, nn, 12, nn, 6, nn, 10],
    ],
    [
        [11, 14, 11, 11, 14, 11, 14, 11, 14, 14, 11, 14],
        [14, 15, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [9, 9, 4, 4, 6, 6, 3, 3, 14, 14, 21, 21],
        [7, 8, 8, 3, 4, 12, 2, 5, 10, 7, 16, 8],
    ],
]


def spin(offsets: list[int], wheels: list[list[list[int]]]):
    for col0 in range(12):
        sum = 0
        for row in range(4):
            for offset, wheel in zip(offsets, wheels):
                col = (col0 + offset) % 12
                if (val := wheel[row][col]) != 0:
                    sum += val
                    break
            if sum > 42:
                break
        else:
            if sum != 42:
                return False
    return True


def get_visible_wheel(offsets: list[int]):
    """print the wheel that is visible from the front"""
    visible_wheel = np.zeros((4, 12), dtype=np.uint8)
    for col0 in range(12):
        for row in range(4):
            for offset, wheel in zip(offsets, wheels):
                col = (col0 + offset) % 12
                if (val := wheel[row][col]) != nn:
                    visible_wheel[row][col0] = val
                    break
            else:
                raise ValueError("no visible wheel")
    return visible_wheel


def get_offsets(wheels):
    # Equivalent to a 5-deep nested for loop
    offsets_iter = itertools.product(range(12), repeat=len(wheels))
    for ii, offsets in enumerate(offsets_iter):
        if spin(offsets, wheels):
            print(f"Found solution at iteration {ii} of {12**len(wheels)}")
            return offsets

offsets = get_offsets(wheels)

# Wheel 4 does not spin
doff = 12 - offsets[4]
offsets = [(offset + doff) % 12 for offset in offsets]
print(f"offsets = {offsets} (drag counterclockwise)")
print("Visible wheel")
vw = get_visible_wheel(offsets)
print(vw)
print()
print("Sum of each column")
print(np.sum(vw, axis=0))
