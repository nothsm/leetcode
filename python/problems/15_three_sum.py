from typing import List, Set, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)
        ts: Set[Tuple[int, int, int]] = set()
        for i in range(len(ns)):
            l: int = i + 1
            r: int = len(ns) - 1
            while l < r:
                s = ns[i] + ns[l] + ns[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ts.add((ns[i], ns[l], ns[r]))
                    l += 1
                    r -= 1
        return [list(t) for t in ts]