use regex::Regex;

fn does_rhyme(sentences: Vec<&str>) -> bool {
    // * Create a regex expression
    let vowels: Regex = Regex::new("[aeiouy]").unwrap();
    // * Create a Vector to save filtered last words
    let mut solutions: Vec<String> = Vec::new();

    // ! Loop through all inputs and filter the vowels of the last Words out
    for s in sentences {
        // ! Lowercase input
        let s: String = s.to_lowercase(); 
        // ! Filter out the last word
        let last_word: &str = s
            .rsplit_once(' ') // ? Split the string at the last occurrence of a space
            .map(|(_, last)| last) // ? return the part after the last space
            .unwrap(); // ? unwrap the option
        // ! Filter out Vowels
        let filtered_vowels: String = last_word
            .chars() // ? Convert to seperate characters
            .filter(|c| vowels.is_match(&c.to_string())) // ? Sort out non Vowels via Regex
            .collect();
        solutions.push(filtered_vowels); // ? Append to Solutions
    }
    // ! Check solutions for correctness
    for index in 0..solutions.len() {
        if index + 1 < solutions.len() {
            if solutions[index] != solutions[index + 1] {
                return false;
            }
        }
    }
    true
}

// Test cases
fn main() {
    // Testing example cases
    println!(
        "Base Examples: {} {} {} {} {}",
        does_rhyme(vec!["Sam I am!", "Green eggs and ham."]),
        does_rhyme(vec!["Sam I am!", "Green eggs and HAM."]),
        does_rhyme(vec!["You're built like a seat", "I bet you like to eat"]),
        does_rhyme(vec!["You are off to the races", "a splendid day."]),
        does_rhyme(vec!["and frequently do?", "you gotta move."])
    );

    println!(
        "\nExtra Examples: {} {}",
        does_rhyme(vec!["Sam I am!", "Green eggs and ham.", "With Sugar and Spam"]),
        does_rhyme(vec!["Sam I am!", "Green eggs and ham.", "With Sugar and Pig"])
    );
}