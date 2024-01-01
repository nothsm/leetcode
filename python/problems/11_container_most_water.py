from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        hs = height
        l: int = 0
        r: int = len(hs) - 1
        max_w = 0
        while l < r:
            w = min(hs[l], hs[r]) * (r - l)
            max_w = max(w, max_w)
            if (hs[l] <= hs[r]):
                l += 1
            elif (hs[r] < hs[l]):
                r -= 1
        return max_w