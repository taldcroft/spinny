# Python

## Run as a command line tool
```
(ska3) ➜  spinny git:(main) time python spinny.py 1000
Found solution in 2517 iterations
offsets = (1, 5, 5, 9, 0) (drag counterclockwise)
Visible wheel
[[10 11  7 11 15  6  8  7  3 14  6  8]
 [21 14 15  9  9 12 11  4 14  7 15 13]
 [ 5  9 10 19  8 12 22 26 16 14  9 13]
 [ 6  8 10  3 10 12  1  5  9  7 12  8]]

Sum of each column
[42 42 42 42 42 42 42 42 42 42 42 42]
python spinny.py 1000  2.41s user 0.07s system 97% cpu 2.530 total
```

## Time function itself in Python
```
In [1]: from spinny import find_meaning_of_life, WHEELS

In [2]: %timeit find_meaning_of_life(WHEELS)
1.4 ms ± 12.5 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```
==> About 1.0 second startup cost for Python and imports

# Rust
```
(ska3) ➜  spinny git:(main) rustc spinny.rs
(ska3) ➜  spinny git:(main) time ./spinny 1000
1 5 5 9 0
./spinny 1000  1.35s user 0.00s system 85% cpu 1.589 total
```

==> Python + numba is impressively FAST!
