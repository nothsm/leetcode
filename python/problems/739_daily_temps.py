class Solution:
    def dailyTemperatures(self, xs: List[int]) -> List[int]:
        acc = []
        ys = [0 for _ in range(len(xs))]
        for i, x in enumerate(xs):
            while acc and x > acc[-1][1]:
                j, _ = acc.pop()
                ys[j] = i - j
            acc.append((i, x))
        return ys