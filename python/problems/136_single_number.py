class Solution:
    def singleNumber(self, xs: List[int]) -> int:
        acc = xs[0]
        for x in xs[1:]:
            acc = acc ^ x
        return acc