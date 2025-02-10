class Solution:
    def myPow(self, x: float, n: int) -> float:
        def go(n):
            if n == 0:
                return 1
            else:
                acc = go(n // 2)
                return (x if n % 2 == 1 else 1) * acc * acc
        return go(n) if n >= 0 else 1 / go(-n)
