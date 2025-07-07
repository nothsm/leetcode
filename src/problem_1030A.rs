use std::io;
use std::io::Read;

fn parse(s: &str) -> Option<Vec<i32>> {
    match s.lines().skip(1).next() {
        Some(line) => Some(
            line.split(' ')
                .map(|word| match word.parse() {
                    Ok(x) => x,
                    Err(_) => panic!(),
                })
                .collect(),
        ),
        None => None,
    }
}

fn solve(xs: Vec<i32>) -> String {
    if xs.iter().sum::<i32>() == 0 {
        String::from("easy")
    } else {
        String::from("hard")
    }
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).expect("bad");

    match parse(s.as_str()) {
        Some(xs) => println!("{}", solve(xs)),
        None => panic!(),
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(90 + 2, 92);
    }

    #[test]
    fn test_parse1() {
        assert_eq!(parse("3\n0 0 1"), Some(vec![0, 0, 1]));
    }

    #[test]
    fn test_parse2() {
        assert_eq!(parse("1\n0"), Some(vec![0]));
    }

    #[test]
    fn test_solve1() {
        assert_eq!(solve(vec![0, 0, 1]), "hard");
    }

    #[test]
    fn test_solve2() {
        assert_eq!(solve(vec![0]), "easy");
    }
}
