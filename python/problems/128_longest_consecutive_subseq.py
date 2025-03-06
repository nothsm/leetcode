def longest_consec(xs):
  def is_starting(x):
    return x - 1 not in xs

  def count_seq(x):
    y = x
    while y in xs:
      y += 1
    return y - x

  return max(map(count_seq, filter(is_starting, xs)), default=0)

class Solution:
    def longestConsecutive(self, xs: List[int]) -> int:
        return longest_consec(set(xs))