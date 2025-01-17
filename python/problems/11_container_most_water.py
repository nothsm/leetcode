class Solution:
    def maxArea(self, xs: List[int]) -> int:
        l = 0
        r = len(xs) - 1
        acc = 0
        while l < r:
            if xs[l] <= xs[r]:
                acc = max(min(xs[l], xs[r]) * (r - l), acc)
                l += 1
                r = r
            else:
                acc = max(min(xs[l], xs[r]) * (r - l), acc)
                l = l
                r -= 1
        return acc
