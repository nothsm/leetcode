B = 32

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(n & 1 << i == 1 << i for i in range(B))