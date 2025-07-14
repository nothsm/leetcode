use std::io;
use std::io::Read;

fn parse(s: &str) -> Vec<(i32, i32)> {
    let mut acc = vec![];
    for line in s.lines().skip(1) {
        match line {
            "10" => acc.push((1, 0)),
            "01" => acc.push((0, 1)),
            _ => panic!(),
        }
    }
    acc
}

fn eval(magnets: &[(i32, i32)]) -> Vec<Vec<(i32, i32)>> {
    let mut acc: Vec<Vec<(i32, i32)>> = vec![];
    for &(l1, r1) in magnets {
        match &mut acc[..] {
            [] => acc.push(vec![(l1, r1)]),
            [.., group] => match group[..] {
                [] => group.push((l1, r1)),
                [.., (l2, _)] if r1 != l2 => group.push((l1, r1)),
                _ => acc.push(vec![(l1, r1)]),
            },
        }
    }
    acc
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).expect("");

    let magnets = parse(&s);
    println!("{}", eval(&magnets).len())
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn parse1() {
        let s = "6\n10\n10\n10\n01\n10\n10";
        let actual = parse(s);
        let expected = vec![(1, 0), (1, 0), (1, 0), (0, 1), (1, 0), (1, 0)];
        assert_eq!(actual, expected);
    }

    #[test]
    fn parse2() {
        let s = "4\n01\n01\n10\n10";
        let actual = parse(s);
        let expected = vec![(0, 1), (0, 1), (1, 0), (1, 0)];
        assert_eq!(actual, expected);
    }

    #[test]
    fn test1() {
        let xs = vec![(1, 0), (1, 0), (1, 0), (0, 1), (1, 0), (1, 0)];
        let actual = eval(&xs);
        assert_eq!(actual.len() as i32, 3)
    }

    #[test]
    fn test2() {
        let xs = vec![(0, 1), (0, 1), (1, 0), (1, 0)];
        let actual = eval(&xs);
        assert_eq!(actual.len() as i32, 2)
    }
}
