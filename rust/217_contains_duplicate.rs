use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(xs: Vec<i32>) -> bool {
        fn go(xs: &[i32], mut acc: HashSet<i32>) -> bool {
            if xs.len() == 0 {
                false
            } else if acc.contains(&xs[0]) {
                true
            } else {
                go(&xs[1..], 
                   {acc.insert(xs[0]); 
                    acc})
            }
        }
        go(&xs[..], HashSet::new())
    }
}