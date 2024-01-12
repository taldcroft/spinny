// Basic program to print hello world

// Defined 2-d array of WHEELS
const WHEELS: [[[i32; 12]; 4]; 5] = [
    [
        [0, 10, 0, 7, 0, 15, 0, 8, 0, 3, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [7, 3, 0, 6, 0, 11, 11, 6, 11, 0, 6, 17],
        [4, 0, 7, 15, 0, 0, 14, 0, 9, 0, 12, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [4, 5, 0, 7, 8, 9, 13, 9, 7, 13, 21, 17],
        [26, 14, 1, 12, 0, 21, 6, 15, 4, 9, 18, 11],
        [0, 16, 0, 9, 0, 5, 0, 10, 0, 8, 0, 22],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 16, 2, 7, 0, 9, 0, 7, 14, 11, 0, 8],
        [8, 9, 0, 9, 20, 12, 3, 6, 0, 14, 12, 3],
        [19, 3, 12, 3, 26, 6, 0, 2, 13, 9, 0, 17],
        [0, 10, 0, 1, 0, 9, 0, 12, 0, 6, 0, 10],
    ],
    [
        [11, 14, 11, 11, 14, 11, 14, 11, 14, 14, 11, 14],
        [14, 15, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [9, 9, 4, 4, 6, 6, 3, 3, 14, 14, 21, 21],
        [7, 8, 8, 3, 4, 12, 2, 5, 10, 7, 16, 8],
    ],
];

fn spin(offsets: [i32; 5]) -> bool {
    for col0 in 0..12 {
        let mut sum = 0;
        for row in 0..4 {
            for iw in 0..5 {
                let offset = offsets[iw];
                let wheel = WHEELS[iw];
                let col = (col0 + offset) % 12;
                let val = wheel[row][col as usize];
                if val != 0 {
                    sum += val;
                    break;
                }
            }
            if sum > 42 {
                break;
            }
        }
        if sum != 42 {
            return false;
        }
    }
    return true;
}

fn get_offsets() -> [i32; 5] {
    // let mut offsets: [i32;5] = [0, 0, 0, 0, 0];
    for i0 in 0..12 {
        for i1 in 0..12 {
            for i2 in 0..12 {
                for i3 in 0..12 {
                    for i4 in 0..12 {
                        let offsets = [i0, i1, i2, i3, i4];
                        if spin(offsets) {
                            return offsets;
                        }
                    }
                }
            }
        }
    }
    return [-1, -1, -1, -1, -1];
}

fn main() {
    // define out as [i32;5]
    let mut out: [i32; 5] = [0, 0, 0, 0, 0];
    for _i in 0..1000 {
        out = get_offsets();
    }
    println!("{} {} {} {} {}", out[0], out[1], out[2], out[3], out[4]);
}
