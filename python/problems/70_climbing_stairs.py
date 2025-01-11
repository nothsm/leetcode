class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1


        def opt(n):
            if n < 0:
                return 0
            elif n == 0:
                return 1
            else:
                return opt(n - 1) + opt(n - 2)

        memo = [0 for _ in range(n + 1)]
        def opt_memo(n):
            memo[0] = 1
            memo[1] = 1 + 0 # memo[0] + memo[-1] <- out of bounds
            for i in range(2, len(memo)):
                memo[i] = memo[i - 1] + memo[i - 2]

        opt_memo(n)
        return memo[n]