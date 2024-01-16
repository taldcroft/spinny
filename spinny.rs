use std::env;
// Basic program to print hello world

// Defined 2-d array of WHEELS
const NN: i32 = 0;
const WHEELS: [[[i32; 12]; 4]; 5] = [
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
];

fn spin_and_check(offsets: [i32; 5]) -> bool {
    let mut sum;
    let mut val;
    let mut col;

    for col0 in 0..12 {
        sum = 0;
        for row in 0..4 {
            for iw in 0..5 {
                col = (col0 + offsets[iw]) % 12;
                val = WHEELS[iw][row][col as usize];
                if val != NN {
                    sum += val;
                    break;
                }
            }
        }
        if sum != 42 {
            return false;
        }
    }
    return true;
}

fn find_meaning_of_life() -> [i32; 5] {
    let mut offsets: [i32; 5];
    for i0 in 0..12 {
        for i1 in 0..12 {
            for i2 in 0..12 {
                for i3 in 0..12 {
                    offsets = [i0, i1, i2, i3, 0];
                    if spin_and_check(offsets) {
                        return offsets;
                    }
                }
            }
        }
    }
    return [-1, -1, -1, -1, -1];
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let iter: i32 = args[1].parse().unwrap_or(1000);

    let mut offsets: [i32; 5] = [0, 0, 0, 0, 0];
    for _i in 0..iter {
        offsets = find_meaning_of_life();
    }

    println!(
        "{} {} {} {} {}",
        offsets[0], offsets[1], offsets[2], offsets[3], offsets[4]
    );
}
