#[macro_use]
extern crate lazy_static;

use std::env;

lazy_static! {
    static ref KEY: String = {
        let chars = [68, 69, 66, 85, 71, 71, 73, 78, 71, 95, 75, 69, 89];
        let mut key = String::new();
        for c in chars.iter() {
            key.push(*c as u8 as char);
        }
        env::var(key).unwrap()
    };
}

fn mm(a: &[usize], b: &[usize], sz: usize) -> Vec<usize> {
    let mut res = vec![0; sz * sz];
    for i in 0..sz {
        for j in 0..sz {
            for k in 0..sz {
                res[i * sz + j] += a[i * sz + k] * b[k * sz + j];
            }
        }
    }
    res
}

fn vm(a: &[usize], b: &[usize], sz: usize) -> Vec<usize> {
    let mut res = vec![0; sz];
    for i in 0..sz {
        for j in 0..sz {
            res[i] += a[i * sz + j] * b[j];
        }
    }
    res
}

static D: [u64; 66] = [36083, 37685, 36445, 37657, 37822, 35848, 34565, 33199, 31214, 33442, 32781, 32399, 34781, 35473, 36661, 35788, 36112, 35885, 38017, 36285, 36747, 38240, 35746, 38025, 37540, 37823, 36702, 35978, 37510, 36367, 36379, 36713, 35388, 35001, 36757, 34842, 31019, 30969, 31111, 31093, 29674, 32334, 35367, 35606, 36125, 35362, 36706, 36294, 32766, 33372, 33187, 34229, 33203, 31603, 37079, 35506, 36933, 36921, 36022, 35279, 32807, 32461, 32168, 30787, 33855, 32102];

fn exit() {
    println!("Wrong!");
    std::process::exit(0);
}

fn main() {
    // Check if one argument was supplied
    if std::env::args().count() != 2 {
        let binary_name = std::env::args().next().unwrap();
        println!("Usage: {} <flag>", binary_name);
        return;
    }

    let flag = std::env::args().nth(1).unwrap();
    let key = KEY.as_str();
    if key.len() > 2 && &key[0..2] == "0N" {
        // Check first 5 characters with a loop
        for i in 0..6 {
            if flag.chars().nth(i).unwrap() != "{ftcbn".chars().nth(5 - i).unwrap() {
                exit();
            }
        }
        // Check last character
        if flag.chars().last().unwrap() != '}' {
            exit();
        }

        // Remove the flag wrapper
        let flag = &flag[6..flag.len() - 1];

        // Check if flag is length 66
        if flag.len() != 66 {
            exit();
        }

        // Check if length of key is 6 
        if key.len() != 6 {
            exit();
        }

        // Load into 6x6 matrix, each row is one shifted from the previous
        let mut mat = vec![0; 36];
        for i in 0..6 {
            for j in 0..6 {
                mat[i * 6 + j] = key.chars().nth((i + j) % 6).unwrap() as usize;
            }
        }

        // Square the matrix
        let sqr = mm(&mat, &mat, 6);
        let known = [25250, 23644, 23619, 24624, 23619, 23644, 23644, 25250, 23644, 23619, 24624, 23619, 23619, 23644, 25250, 23644, 23619, 24624, 24624, 23619, 23644, 25250, 23644, 23619, 23619, 24624, 23619, 23644, 25250, 23644, 23644, 23619, 24624, 23619, 23644, 25250];

        // Check if the matrix is correct
        for i in 0..36 {
            if sqr[i] != known[i] {
                exit();
            }
        }

        // Load the flag in chunks of vectors of size 6
        // Then multiply each chunk by the matrix
        // And check if the result is equal to the static array D
        for i in 0..11 {
            let mut chunk = vec![0; 6];
            for j in 0..6 {
                chunk[j] = flag.chars().nth(i * 6 + j).unwrap() as usize;
            }
            let res = vm(&mat, &chunk, 6);
            for j in 0..6 {
                if res[j] != D[i * 6 + j] as usize {
                    exit();
                }
            }
        }
        
        println!("Correct!");
    }
    else {
        println!("Go look somewhere else");
    }
}

