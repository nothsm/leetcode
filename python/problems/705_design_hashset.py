from operator import *

LOAD_FACTOR = 0.7

def inc(x):
  return add(x, 1)

def dec(x):
  return sub(x, 1)

def double(x):
  return mul(x, 2)

def hash_ix(xs, k):
  return mod(hash(k), len(xs))

def hash_contains(xs, k):
  return contains(xs[hash_ix(xs, k)], k)

def hash_insert(xs, k):
  if not_(hash_contains(xs, k)):
    xs[hash_ix(xs, k)].append(k)
    return k
  return False

def hash_remove(xs, k):
  if hash_contains(xs, k):
    xs[(hash_ix(xs, k))].remove(k)
    return k
  return False

class MyHashSet:
    def __init__(self):
      self.buckets = [[] for _ in range(53)]
      self.n = 0
        
    def load_factor(self):
      return truediv(self.n, len(self.buckets))

    def rebalance(self):
      buckets = [[] for _ in range(double(len(self.buckets)))]
      for xs in self.buckets:
        for x in xs:
          buckets[mod(hash(x), len(buckets))].append(x)
      self.buckets = buckets

    def add(self, key: int) -> None:
      if le(LOAD_FACTOR, self.load_factor()):
        self.rebalance()

      hash_insert(self.buckets, key)
      self.n = inc(self.n)
        
    def remove(self, key: int) -> None:
      hash_remove(self.buckets, key)
      self.n = dec(self.n)
        
    def contains(self, key: int) -> bool:
      return hash_contains(self.buckets, key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)