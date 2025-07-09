use std::io;

fn f(n: i64) -> i64 {
    let acc: i64 = ((n + 1) / 2) * ((-1 as i64).pow((n % 2) as u32));
    acc
}

fn read() -> i64 {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    s.trim().parse().expect("cant parse int")
}

fn main() {
    println!("{}", f(read()));
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test1() {
        assert_eq!(f(4), 2);
    }

    #[test]
    fn test2() {
        assert_eq!(f(5), -3);
    }
}
