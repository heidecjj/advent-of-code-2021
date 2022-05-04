use std::time::Instant;
use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let now = Instant::now();
    let num_increases = match part1() {
        Ok(x) => x,
        Err(_) => 0
    };
    let elapsed = now.elapsed();
    println!("Part 1 ({:.2?}): {}", elapsed, num_increases);

    let now = Instant::now();
    let num_increases = match part2() {
        Ok(x) => x,
        Err(_) => 0
    };
    let elapsed = now.elapsed();
    println!("Part 2 ({:.2?}): {}", elapsed, num_increases);
}

fn read(path: &str) -> Result<Vec<u32>, io::Error> {
    let file = File::open(path)?;
    let br = io::BufReader::new(file);
    let mut v = Vec::new();
    for line in br.lines() {
        let line = line?;
        let n = line.trim().parse().map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))?;
        v.push(n);
    }
    Ok(v)
}

fn part1() -> Result<u32, io::Error> {
    let mut increases: u32 = 0;
    let mut prev: u32 = 0;
    for num in read("input.txt")? {
        if num > prev {
            increases += 1;
        }
        prev = num;
    }

    Ok(if increases > 0 {increases - 1} else {0})
}


fn part2() -> Result<u32, io::Error> {
    let mut increases: u32 = 0;
    let nums = read("input.txt")?;
    for i in 0..(nums.len() - 3) {
        if nums[i + 3] > nums[i] {
            increases += 1; 
        }
    }

    Ok(increases)
}
