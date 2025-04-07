use std::collections::HashSet;
use std::hash::Hash;

fn count_unique<I, T>(xs: I) -> usize
where
  I: Iterator<Item = T>,
  T: Eq + Hash
{
  xs.collect::<HashSet<_>>().len()
}

impl Solution {
    pub fn contains_duplicate(xs: Vec<i32>) -> bool {
        count_unique(xs.iter()) != xs.len()
    }
}
