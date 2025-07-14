use std::io;

fn read() -> Vec<i32> {
    io::stdin().read_line(&mut String::new()).expect("");

    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("cant read s");

    s.trim()
        .split(' ')
        .map(|word| word.parse().expect("cant parse"))
        .collect()
}

fn mean(xs: &Vec<i32>) -> f64 {
    let acc = xs.into_iter().sum::<i32>() as f64;
    let n = xs.len() as f64;
    acc / n
}

fn main() {
    println!("{}", mean(&read()));
}
