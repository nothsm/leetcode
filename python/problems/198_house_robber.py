class Solution:
    def rob(self, xs: List[int]) -> int:
        def go(i, acc):
            if i >= len(xs):
                return acc
            else:
                return max(go(i + 2, acc + xs[i]), go(i + 1, acc))


        def dp(acc):
            def go(i):
                if i == len(xs):
                    return acc
                elif i == 0:
                    acc[i] = max(0, 0 + xs[i])
                    return go(i + 1)
                elif i == 1:
                    acc[i] = max(acc[i - 1], 0 + xs[i])
                    return go(i + 1)
                else:
                    acc[i] = max(acc[i - 1], acc[i - 2] + xs[i])
                    return go(i + 1)
            return go(0)

        return dp([0 for _ in range(len(xs))])[-1]