class Solution:
    def trap(self, xs: List[int]) -> int:
        acc = 0
        ls = []
        for x in xs:
            ls.append(acc)
            acc = max(x, acc)

        acc = 0
        rs = []
        for x in reversed(xs):
            rs.append(acc)
            acc = max(x, acc)
        rs = reversed(rs)
        
        acc = 0
        for l, r, x in zip(ls, rs, xs):
            acc += max(min(l, r) - x, 0)

        return acc
