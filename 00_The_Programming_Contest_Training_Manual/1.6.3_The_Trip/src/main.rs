use std::fs;

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

fn main() {
    let all_tripcosts = parse_trip_costs("./data/ques_00.txt");

    println!("{:?}", all_tripcosts);
}
