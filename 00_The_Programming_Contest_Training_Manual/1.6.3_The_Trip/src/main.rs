use std::cmp;
use std::fs;
use std::io::Write;

fn parse_trip_costs(filepath: &str) -> Vec<Vec<u32>> {
    let contents = fs::read_to_string(String::from(filepath)).unwrap();

    /* Storage for the trip costs. */
    let mut costs: Vec<u32> = Vec::new();
    let mut all_costs: Vec<Vec<u32>> = Vec::new();

    /* Iterate over the string and consume it. */
    for line in contents.lines() {
        /* The file ends with a "0" */
        if line == "0" {
            all_costs.push(costs.clone());
            break;

        /* Detect the start of a new trip. */
        } else if !line.contains(".") {
            /* Save the costs. */
            if !costs.is_empty() {
                all_costs.push(costs.clone());
                costs.clear();
            }

            /* Detect the number of pupils on the trip. */
            let students: usize = line.parse().unwrap();

            /* Allocate space for an array of travel costs. */
            costs.reserve(students);
        } else {
            /* Otherwise save the amount to an array. */
            let raw_cost: u32 = line.replace(".", "").parse().unwrap();
            costs.push(raw_cost);
        }
    }
    return all_costs;
}

fn min_exchange(costs: Vec<u32>) -> u32 {
    /* Calculate the average ammount spent of the trip. */
    let avg: u32 = costs.iter().sum::<u32>() / (costs.len() as u32);

    let mut sum_low: u32 = 0;
    let mut sum_hig: u32 = 0;

    /* Calculate the sum of the amount above and below the average. */
    for ind_cst in costs {
        if ind_cst > avg {
            sum_hig += ind_cst - avg;
        } else {
            sum_low += avg - ind_cst;
        }
    }
    return cmp::min(sum_low, sum_hig);
}

fn create_output(in_file: &str, out_file: &str) {
    let mut buffer = fs::File::create(out_file).unwrap();

    /* Parse the input file. */
    let all_tripcosts = parse_trip_costs(in_file);

    for raw_cost in all_tripcosts {
        /* Calculate the minimum exchange cost. */
        let raw_exc: f64 = min_exchange(raw_cost) as f64 / 100.00;
        let result = format!("£{:.2}\n", raw_exc);

        println!("{}", result);

        /* Output to a text file. */
        buffer.write(result.as_bytes()).unwrap();
    }
}

fn main() {
    create_output("./data/ques_00.txt", "./data/test_00.txt");
}
