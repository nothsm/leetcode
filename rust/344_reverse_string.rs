pub fn swap(xs: &mut Vec<char>, i: usize, j: usize) {
    (xs[i], xs[j]) = (xs[j], xs[i]);
  }
  
  impl Solution {
      pub fn reverse_string(s: &mut Vec<char>) {
        fn go(s: &mut Vec<char>, l: usize, r: usize) {
          if (r as isize) - (l as isize) <= 0 {
            return;
          } else {
            swap(s, l, r);
            go(s, l + 1, r - 1);
          }
        }
        go(s, 0, s.len() - 1);
      }
  }