class Solution:
    def missingNumber(self, xs: List[int]) -> int:
        acc = len(xs)
        for i, x in enumerate(xs):
            acc = acc ^ i ^ x
        return acc
        