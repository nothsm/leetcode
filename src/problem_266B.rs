use std::io;

fn swap(xs: &mut Vec<char>, i: usize, j: usize) {
    (xs[i], xs[j]) = (xs[j], xs[i])
}

fn eval(mut xs: Vec<char>, n: i32) -> Vec<char> {
    let mut acc = n;
    while acc > 0 {
        let mut i = 0;
        while i < xs.len() - 1 {
            if xs[i] == 'B' && xs[i + 1] == 'G' {
                swap(&mut xs, i, i + 1);
                i += 1;
            }
            i += 1;
        }
        acc -= 1;
    }
    xs
}

fn parse_n(s: &str) -> Result<i32, i32> {
    let words: Vec<&str> = s.split(' ').collect();
    if words.len() == 2 {
        match words[1].parse() {
            Ok(n) => Ok(n),
            Err(_) => Err(-1)
        }
    } else {
        Err(-1)
    }
}

fn parse_queue(s: &str) -> Result<Vec<char>, i32> {
    Ok(s.chars().collect())
}

fn main() {
    let mut s_n = String::new();
    io::stdin()
        .read_line(&mut s_n)
        .expect("bad input");

    let mut s_queue = String::new();
    io::stdin()
        .read_line(&mut s_queue)
        .expect("bad input");

    let n = parse_n(s_n.trim()).expect("bad");
    let xs = parse_queue(s_queue.trim()).expect("bad");

    let acc = eval(xs, n);
    let out: String = acc.into_iter().collect();
    println!("{}", out);
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_swap() {
        let mut xs = vec!['a', 'b', 'c'];
        swap(&mut xs, 0, 1);
        assert_eq!(xs, vec!['b', 'a', 'c']);
    }

    #[test]
    fn test1() {
        assert_eq!(eval(vec!['B', 'G', 'G', 'B', 'G'], 1), vec!['G', 'B', 'G', 'G', 'B'])
    }

    #[test]
    fn test2() {
        assert_eq!(eval(vec!['B', 'G', 'G', 'B', 'G'], 2), vec!['G', 'G', 'B', 'G', 'B'])
    }

    #[test]
    fn test3() {
        assert_eq!(eval(vec!['G', 'G', 'G', 'B'], 1), vec!['G', 'G', 'G', 'B'])
    }

    #[test]
    fn test_parse_n1() {
        assert_eq!(parse_n("5 1"), Ok(1));
    }


    #[test]
    fn test_parse_n2() {
        assert_eq!(parse_n("5 2"), Ok(2));
    }


    #[test]
    fn test_parse_n3() {
        assert_eq!(parse_n("4 1"), Ok(1));
    }

    #[test]
    fn test_parse_queue1() {
        assert_eq!(parse_queue("BGGBG"), Ok(vec!['B', 'G', 'G', 'B', 'G']));
    }

    #[test]
    fn test_parse_queue3() {
        assert_eq!(parse_queue("GGGB"), Ok(vec!['G', 'G', 'G', 'B']));
    }
}
