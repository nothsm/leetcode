class Solution:
    def twoSum(self, xs: List[int], t: int) -> List[int]:
        l = 0
        r = len(xs) - 1
        while r - l > 0:
            v = xs[l] + xs[r]
            if v < t:
                l += 1
            elif v > t:
                r -= 1
            elif v == t:
                return [l + 1, r + 1]