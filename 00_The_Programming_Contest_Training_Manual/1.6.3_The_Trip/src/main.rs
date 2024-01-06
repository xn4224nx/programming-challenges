use std::fs;
use std::cmp;

fn parse_trip_costs(filepath: &str) -> Vec<Vec<u32>> {

    let contents = fs::read_to_string(String::from(filepath)).unwrap();

    /* Storage for the trip costs. */
    let mut costs: Vec<u32> = Vec::new();
    let mut all_costs: Vec<Vec<u32>> = Vec::new();

    /* Iterate over the string and consume it. */
    for line in contents.lines() {
        /* The file ends with a "0" */
        if line == "0" {
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


fn main() {
    let all_tripcosts = parse_trip_costs("./data/ques_00.txt");
    
    for raw_cost in all_tripcosts {
        println!("{}", min_exchange(raw_cost));
    }
}
