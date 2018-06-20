#[allow(unused_must_use)]
fn read_int() -> i32 {
    let mut input: String = String::new();
    std::io::stdin().read_line(&mut input);
    input.trim().parse::<i32>().unwrap()
}


fn main() {
    let h1 = read_int();
    let h2 = read_int();
    println!("{}", h1 - h2);
}
