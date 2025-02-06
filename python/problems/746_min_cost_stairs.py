class Solution:
    def minCostClimbingStairs(self, xs: List[int]) -> int:
        N = len(xs)

        def go(n, acc):
            if n < 0:
                return float('inf')
            elif n == 0:
                return acc
            else:
                acc += xs[n - 1]
                return min(go(n - 1, acc), go(n - 2, acc))

        def dp(i, acc):
            if i == N:
                acc[i] = min(acc[i-1], acc[i-2])
                return
            else:
                acc[i] = xs[i] + min(acc[i - 1], acc[i - 2])
                dp(i + 1, acc)
        
        acc = [0 for _ in range(N + 1)]
        acc[0] = xs[0]
        acc[1] = xs[1]
        dp(2, acc)
        return acc[-1] # return min(go(N, 0), go(N-1, 0))