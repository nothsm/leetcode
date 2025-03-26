from operator import *

def inc(i):
  return add(i, 1)

def is_nonneg(x):
  return le(0, x)

def startswith(s, pre):
  def go(i):
    if eq(i, len(pre)):
      return True
    else:
      return eq(s[i], pre[i]) and go(inc(i))
  return go(0)

def butlast(xs):
  return xs[:-1]

class Solution:
    def longestCommonPrefix(self, xs: List[str]) -> str:
        pre = min(xs, key=len)
        def go(i, acc):
          assert is_nonneg(i)
          assert le(i, len(pre))
          assert eq(acc, pre[:i]), (acc, pre[:i])

          if not_(all(map(lambda x: startswith(x, acc), xs))):
            return butlast(acc)
          elif eq(i, len(pre)):
            assert eq(acc, pre)
            return acc
          else:
            assert lt(len(acc), len(pre))
            return go(inc(i), add(acc, pre[i]))
        if not_(pre):
          return ""
        else:
          return go(0, "")