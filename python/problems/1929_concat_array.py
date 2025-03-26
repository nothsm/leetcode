from operator import *

def is_zero(x):
  return eq(x, 0)

def dec(x):
  return x - 1

class Solution:
    def getConcatenation(self, xs: List[int]) -> List[int]:
      N = len(xs)
      def go(n, acc):
        assert le(len(acc), n)
        if is_zero(sub(n, len(acc))):
          return acc
        else:
          acc.append(getitem(xs, mod(len(acc), N)))
          return go(n, acc)
      return go(mul(2, N), [])

        