class Solution:
    def maxProfit(self, xs: List[int]) -> int:
        acc = 0
        l = 0
        r = 1
        while l < r and r < len(xs):
            if xs[r] < xs[l]:
                acc = max(xs[r] - xs[l], acc)
                l = r
                r += 1
            elif xs[r] >= xs[l]:
                acc = max(xs[r] - xs[l], acc)
                r += 1
        return acc