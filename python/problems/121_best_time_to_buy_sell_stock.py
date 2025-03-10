class Solution:
    def maxProfit(self, xs: List[int]) -> int:
        l = 0
        r = l + 1
        acc = 0
        while r < len(xs):
            acc = max(xs[r] - xs[l], acc)
            if xs[r] < xs[l]:
                l = r
                r = l + 1
            else:
                r += 1
        return acc