fn num_to_str(num: u32, size: usize) -> String {
    /* Strings to hold the output */
    let mut top = String::new();
    let mut mid1: Vec<String> = vec![String::new(); size];
    let mut half = String::new();
    let mut mid2: Vec<String> = vec![String::new(); size];
    let mut low = String::new();

    /* Convert the number to a string and iterate over every char */
    for digit in num.to_string().chars() {
        /* Create the top part of the number. */
        if digit == '1' || digit == '4' {
            top.push_str(&" ".repeat(size + 2))
        } else {
            top.push(' ');
            top.push_str(&"-".repeat(size));
            top.push(' ');
        }

        /* Create the first middle string. */
        for mid_level in &mut mid1 {
            if digit == '4' || digit == '8' || digit == '9' || digit == '0' {
                mid_level.push('|');
                mid_level.push_str(&" ".repeat(size));
                mid_level.push('|');
            } else if digit == '5' || digit == '6' {
                mid_level.push('|');
                mid_level.push_str(&" ".repeat(size));
                mid_level.push(' ');
            } else {
                mid_level.push(' ');
                mid_level.push_str(&" ".repeat(size));
                mid_level.push('|');
            }
        }

        /* Create the half way string */
        if digit == '1' || digit == '7' || digit == '0' {
            half.push_str(&" ".repeat(size + 2));
        } else {
            half.push(' ');
            half.push_str(&"-".repeat(size));
            half.push(' ');
        }

        /* Create the second middle string */
        for mid_level in &mut mid2 {
            if digit == '0' || digit == '8' || digit == '6' {
                mid_level.push('|');
                mid_level.push_str(&" ".repeat(size));
                mid_level.push('|');
            } else if digit == '2' {
                mid_level.push('|');
                mid_level.push_str(&" ".repeat(size));
                mid_level.push(' ');
            } else {
                mid_level.push_str(&" ".repeat(size + 1));
                mid_level.push('|');
            }
        }

        /* Create the bottom string */
        if digit == '1' || digit == '4' || digit == '7' {
            low.push_str(&" ".repeat(size + 2));
        } else {
            low.push(' ');
            low.push_str(&"-".repeat(size));
            low.push(' ');
        }

        /* Add the space between numbers */
        top.push_str("  ");
        mid1.iter_mut().for_each(|v| v.push_str("  "));
        half.push_str("  ");
        mid2.iter_mut().for_each(|v| v.push_str("  "));
        low.push_str("  ");
    }

    /* Finish off the strings with a new line */
    top.push('\n');
    mid1.iter_mut().for_each(|v| v.push('\n'));
    half.push('\n');
    mid2.iter_mut().for_each(|v| v.push('\n'));
    low.push('\n');

    /* Combine all the strings */
    return top + &mid1.join("") + &half + &mid2.join("") + &low;
}

fn main() {
    println!("{}", num_to_str(1234567890, 3));
}
