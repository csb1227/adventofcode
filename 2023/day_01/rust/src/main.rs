use std::fs;
use regex::Regex;

fn main() {
    let input: Vec<String> = read_input(String::from("C:/dev/adventofcode/2023/day_01/input.txt"));
    let numbers: Vec<Vec<i32>> = extract_numbers(input);

    let calibration_values = get_calibration_values(numbers);

    println!("{}", sum_calibration_values(calibration_values));
}

fn read_input(file_path : String) -> Vec<String> {
    return fs::read_to_string(file_path).unwrap().split("\n").map(String::from).collect();

}

fn extract_numbers(input : Vec<String>) -> Vec<Vec<i32>> {
    let re = Regex::new(r"\d").unwrap();
    let mut result: Vec<Vec<i32>> = vec![];

    for calibration_value in input {
        let mut x: Vec<i32> = vec![];
        for capture in re.captures_iter(&calibration_value) {
            if let Some(number_str) = capture.get(0) {
                if let Ok(number) = number_str.as_str().parse::<i32>() {
                    x.push(number);
                }
            }
        }

        result.push(x);
    }

    return result;
}

fn get_calibration_values(input: Vec<Vec<i32>>) -> Vec<i32>{
    let mut result: Vec<i32> = vec![];

    for i in input {
        result.push((i[0] * 10) + i[i.len() - 1]);
    }

    return result;
}

fn sum_calibration_values(input: Vec<i32>) -> i32 {
    return input.iter().sum();
}