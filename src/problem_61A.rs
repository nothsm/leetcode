use std::io;

fn interpret(bitstring: &str) -> u128 {
    let bitstring: Vec<u8> = bitstring.as_bytes().into_iter().map(|&c| c).rev().collect();

    let mut acc = 0;
    let mut i = 0;
    while i < bitstring.len() {
        acc += 2_u128.pow(i as u32) * ((bitstring[i] - b'0') as u128);
        i += 1;
    }
    acc
}

fn main() {
    let mut first_line = String::new();
    let mut second_line = String::new();

    io::stdin()
        .read_line(&mut first_line)
        .expect("couldnt read first line");
    io::stdin()
        .read_line(&mut second_line)
        .expect("couldnt read second line");

    let x = first_line.trim();
    let y = second_line.trim();

    println!("{:0width$b}", interpret(x) ^ interpret(y), width = x.len());
}
