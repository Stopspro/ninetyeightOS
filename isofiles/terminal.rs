use std::io;

fn main() {
  let term input = String::new();

  io::stdin().read_line(&term input)
    .expect("Failed to read line");
