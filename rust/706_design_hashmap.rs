static BUCKETS: usize = 7;
static LOAD_FACTOR: f32 = 0.66;

struct MyHashMap {
  n: usize,
  xss: Vec<Vec<(i32,i32)>>,
}

fn assoc_mut(xs: &mut Vec<(i32, i32)>, key: i32) -> Option<&mut (i32, i32)> {
  xs.iter_mut()
    .filter(|(k, _)| *k == key)
    .next()
}

fn lookup_mut(xss: &mut Vec<Vec<(i32, i32)>>, key: i32) -> &mut Vec<(i32, i32)> {
    let ix = (key % xss.len() as i32) as usize;
    &mut xss[ix]
}

fn lookup(xss: &Vec<Vec<(i32, i32)>>, key: i32) -> &Vec<(i32, i32)> {
  &xss[(key % xss.len() as i32) as usize]
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashMap {

    fn new() -> Self {
        MyHashMap {
          n: 0,
          xss: vec![vec![]; BUCKETS],
        }
    }

    fn put(&mut self, key: i32, value: i32) {
      let mut xs = lookup_mut(&mut self.xss, key);
      match assoc_mut(xs, key) {
        Some((k, v)) => *v = value,
        None => xs.push((key, value)),
      }
      self.n += 1;
    }

    fn get(&self, key: i32) -> i32 {
      match ((*lookup(&self.xss, key))
            .iter()
            .filter(|&&(k, v)| k == key)
            .next()) {
              Some(&(k, v)) => v,
              None => -1
            }
    }

    fn remove(&mut self, key: i32) {
      (*lookup_mut(&mut self.xss, key)).retain(|&(k, v)| k != key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap::new();
 * obj.put(key, value);
 * let ret_2: i32 = obj.get(key);
 * obj.remove(key);
 */
