use std::io;

fn uniq(xs: &Vec<i32>) -> Vec<i32> {
    let mut i = 0;
    let mut acc = vec![];

    // Inv: acc is the uniq elements of [xs[0], ..., xs[i - 1]]
    while i < xs.len() {
        if !acc.contains(&xs[i]) {
            acc.push(xs[i]);
        }
        i += 1;
    }
    acc
}

fn eval(xs: &Vec<i32>) -> i32 {
    let uniqs = uniq(xs);
    assert!(xs.len() >= uniqs.len());

    let diff = (xs.len() - uniqs.len()) as i32;
    assert!(diff >= 0);

    diff
}

fn read() -> Vec<i32> {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("couldnt read input");

    let words: Vec<&str> = s.trim().split(' ').collect();
    // assert!((words.len() * 2) - 1 == s.len());

    let mut i = 0;
    let mut acc = vec![];
    // Inv: acc is the ints of [words[0], ..., words[i - 1]]
    while i < words.len() {
        acc.push(words[i].parse().expect("couldnt parse int"));
        i += 1;
    }
    assert!(i == words.len());
    assert!(words.len() == acc.len());
    acc
}

fn main() {
    let xs = read();
    let horseshoes = eval(&xs);
    println!("{}", horseshoes);
}
