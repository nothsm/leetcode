from operator import *

def is_nonneg(i):
  return le(0, i)

def inc(x):
  return add(x, 1)

def swap(xs, l, r):
  temp = xs[r]
  xs[r] = xs[l]
  xs[l] = temp

class Solution:
    def removeElement(self, xs: List[int], t: int) -> int:
      n = len(xs)
      def go(i, l, acc):
        assert is_nonneg(i)
        assert le(i, n)
        assert le(l, n)
        # assert all(map(lambda x: ne(x, t), xs[0:l])), (xs, xs[0:l])

        if n - i == 0:
          return acc
        elif ne(xs[i], t):
          swap(xs, l, i)
          return go(inc(i), inc(l), inc(acc))
        else:
          return go(inc(i), l, acc)

      return go(0, 0, 0)
        