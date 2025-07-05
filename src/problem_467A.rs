use std::io;
use std::io::Read;

fn parse_rooms(s: &str) -> Result<Vec<(i32, i32)>, i32> {
    let mut acc = vec![];
    let lines = s.lines();
    for line in lines {
        let words: Vec<&str> = line.split(' ').collect();
        if words.len() == 2 {
            match (words[0].parse(), words[1].parse()) {
                (Ok(p), Ok(q)) => acc.push((p, q)),
                _ => return Err(-1)
            }
        } else {
            return Err(-1)
        }
    }
    Ok(acc)
}

fn solve(xs: &Vec<(i32, i32)>) -> i32 {
    let mut acc = 0;
    for (p, q) in xs {
        if q - p >= 2 {
            acc += 1
        }
    }
    acc
}

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut String::new()).expect("");
    io::stdin().read_to_string(&mut s).expect("bad input format");

    let xs = parse_rooms(s.as_str()).expect("bad input format");
    println!("{}", solve(&xs));
}


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn parse_1() {
        let s = "1 1\n2 2\n3 3\n";
        let expected = Ok(vec![(1, 1), (2, 2), (3, 3)]);
        assert_eq!(parse_rooms(s), expected);
    }


    #[test]
    fn parse_2() {
        let s = "1 10\n0 10\n10 10\n";
        let expected = Ok(vec![(1, 10), (0, 10), (10, 10)]);
        assert_eq!(parse_rooms(s), expected);
    }

    #[test]
    fn solve_1() {
        let xs = vec![(1, 1), (2, 2), (3, 3)];
        let expected = 0;
        assert_eq!(solve(&xs), expected);
    }

    #[test]
    fn solve_2() {
        let xs = vec![(1, 10), (0, 10), (10, 10)];
        let expected = 2;
        assert_eq!(solve(&xs), expected);
    }
}
