use std::collections::HashMap;

/// Execute one step in the hailstone cycle.
fn hail_step(start_n: u32) -> u32 {
    if start_n % 2 == 0 {
        return start_n / 2;
    } else {
        return 3 * start_n + 1;
    }
}

/// Find the maximum hailstone cycles for a range of numbers.
fn max_hail_cycles(start_h: u32, end_h: u32) -> u32 {
    let mut max_cycle = 0;
    let mut prev_cycles: HashMap<u32, u32> = HashMap::new();

    for initial_h in start_h..=end_h {
        let mut tmp_cycle_cnt = 1;
        let mut tmp_hail = initial_h;

        /* Run the whole hail stone path. */
        while tmp_hail != 1 {
            tmp_hail = hail_step(tmp_hail);

            /* Check to see if the hail path has seen before */
            if prev_cycles.contains_key(&tmp_hail) {
                tmp_cycle_cnt += prev_cycles[&tmp_hail];
                break;
            } else {
                tmp_cycle_cnt += 1;
            }
        }

        /* Test for a new highest cycle. */
        if tmp_cycle_cnt > max_cycle {
            max_cycle = tmp_cycle_cnt;
        }

        /* Save the cycle length of the current start number. */
        prev_cycles.insert(initial_h, tmp_cycle_cnt);
    }

    return max_cycle;
}

fn main() {
    assert_eq!(max_hail_cycles(1, 10), 20);
    assert_eq!(max_hail_cycles(100, 200), 125);
    assert_eq!(max_hail_cycles(201, 210), 89);
    assert_eq!(max_hail_cycles(900, 1000), 174);
}
