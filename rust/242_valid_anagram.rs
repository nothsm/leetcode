use std::collections::HashMap;
use std::hash::Hash;

fn frequencies<I, T>(xs: I) -> HashMap<T, usize>
where
  I: Iterator<Item = T>,
  T: Eq + Hash
{
  fn step<T>(mut acc: HashMap<T, usize>, x: T) -> HashMap<T, usize>
  where
    T: Eq + Hash
  {
    *acc.entry(x).or_insert(0) += 1;
    acc
  }

  xs.fold(HashMap::new(), step)
}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        frequencies(s.chars()) == frequencies(t.chars())
    }
}
