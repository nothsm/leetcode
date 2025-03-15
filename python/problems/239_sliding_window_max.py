class Solution:
    def maxSlidingWindow(self, xs: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        wd = {}
        M = -1001
        acc = []
        while r < len(xs):
            if r - l < k:
                wd[xs[r]] = wd.get(xs[r], 0) + 1
                M = max(xs[r], M)
                r += 1
            elif wd[xs[l]] == 1 and xs[l] == M:
                acc.append(M)
                del wd[xs[l]]
                wd[xs[r]] = wd.get(xs[r], 0) + 1
                M = max(wd)
                l += 1
                r += 1
            elif wd[xs[l]] == 1 and xs[l] != M:
                acc.append(M)
                del wd[xs[l]]
                wd[xs[r]] = wd.get(xs[r], 0) + 1
                M = max(xs[r], M)
                l += 1
                r += 1
            elif wd[xs[l]] > 1:
                acc.append(M)
                wd[xs[l]] -= 1
                wd[xs[r]] = wd.get(xs[r], 0) + 1
                M = max(xs[r], M)
                l += 1
                r += 1
        acc.append(M)
        return acc

        