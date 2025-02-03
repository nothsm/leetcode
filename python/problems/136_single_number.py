def bag(xs):
    ys = {}
    for x in xs:
        ys[x] = ys.get(x, 0) + 1
    return ys

class Solution:
    def singleNumber(self, xs: List[int]) -> int:
        ys = bag(xs)
        for x in xs:
            if ys[x] == 1:
                return x