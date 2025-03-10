class Solution:
    def threeSum(self, xs: List[int]) -> List[List[int]]:
        xs = sorted(xs)

        seen = set()
        acc = []
        for i, x in enumerate(xs[:-1]):
            t = -x
            l = i + 1
            r = len(xs) - 1
            while r - l > 0:
                v = xs[l] + xs[r]
                if v < t:
                    l += 1
                elif v == t:
                    tp = (xs[i], xs[l], xs[r])
                    if tp not in seen:
                        seen.add(tp)
                        acc.append(list(tp))
                    l += 1
                elif v > t:
                    r -= 1
        return acc
