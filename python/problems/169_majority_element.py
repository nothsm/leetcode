from operator import *

def is_zero(x):
  return eq(x, 0)

def inc(x):
  return add(x, 1)

def dec(x):
  return sub(x, 1)

class Solution:
    def majorityElement(self, xs: List[int]) -> int:
      v = None
      ct = 0
      for x in xs:
        if is_zero(ct):
          v = x
          ct = inc(ct)
        elif eq(x, v):
          ct = inc(ct)
        elif ne(x, v):
          ct = dec(ct)
      return v
        