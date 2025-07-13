use std::io;

fn assoc(i: i32, assocs: &Vec<(i32, i32)>) -> Option<i32> {
    for &(k, v) in assocs {
        if k == i {
            return Some(v);
        }
    }
    None
}

fn eval(ps: &Vec<i32>) -> Vec<i32> {
    let mut send = vec![];
    let mut recv: Vec<(i32, i32)> = vec![];
    for (i, &p) in ps.iter().enumerate() {
        send.push(((i + 1) as i32, p));
    }

    for &(sender, receiver) in &send {
        recv.push((receiver, sender));
    }

    (1..=ps.len())
        .into_iter()
        .map(|i| assoc(i as i32, &recv).unwrap())
        .collect()
}

fn digits(x: i32) -> Vec<i32> {
    assert!(x > 0);
    let mut cur = x;
    let mut acc = vec![];
    while cur > 0 {
        acc.push(x % 10);
        cur = cur / 10;
    }
    acc.reverse();
    acc
}

fn my_show(xs: &Vec<i32>) -> Vec<char> {
    let mut acc = vec![];
    if let Some((&last, xs)) = xs.split_last() {
        for &x in xs {
            let mut ds = digits(x)
                .into_iter()
                .map(|d| char::from_digit(d as u32, 10).unwrap())
                .collect();
            acc.append(&mut ds);
            acc.push(' ');
        }
        let mut ds = digits(last)
            .into_iter()
            .map(|d| char::from_digit(d as u32, 10).unwrap())
            .collect();
        acc.append(&mut ds);
    }
    acc
}

fn read() -> Option<Vec<i32>> {
    io::stdin().read_line(&mut String::new()).expect("");

    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");

    let mut acc = vec![];
    for word in s.trim().split(' ') {
        match word.parse::<i32>() {
            Err(_) => return None,
            Ok(n) => acc.push(n),
        }
    }
    Some(acc)
}

fn main() {
    let s: String = my_show(&eval(&read().unwrap())).into_iter().collect();
    println!("{}", s)
}
