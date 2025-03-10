class Solution:
    def trap(self, xs: List[int]) -> int:
        l = 0
        r = len(xs) - 1
        L = xs[l]
        R = xs[r]
        acc = 0
        while r - l > 0:
            if L <= R:
                l += 1
                acc += max(L - xs[l], 0)
                L = max(xs[l], L)
            elif R < L:
                r -= 1
                acc += max(R - xs[r], 0)
                R = max(xs[r], R)
        return acc
