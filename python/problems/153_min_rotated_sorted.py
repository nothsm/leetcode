class Solution:
    def findMin(self, xs: List[int]) -> int:
        def go(l, r, acc):
            m = (l + r) // 2
            acc = min([xs[l], xs[r], xs[m], acc])
            if r - l <= 1:
                return acc
            elif xs[m] >= xs[l]:
                return go(m + 1, r, acc)
            else:
                return go(l, m - 1, acc)
        
        if len(xs) < 2:
            return xs[0]
        else:
            l = 0
            r = len(xs) - 1
            acc = min(xs[0], xs[-1])
            return go(l, r, acc)