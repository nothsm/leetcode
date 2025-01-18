class Solution:
    def threeSum(self, xs: List[int]) -> List[List[int]]:
        xs = sorted(xs)
        ys = []
        uniq = set()
        for i, x in enumerate(xs):
            t = -x
            l = i + 1
            r = len(xs) - 1
            acc = []
            while l < r:
                if xs[l] + xs[r] == t:
                    acc.append((xs[l], xs[r]))
                    l += 1
                    r = r
                elif xs[l] + xs[r] < t:
                    l += 1
                    r = r
                elif xs[l] + xs[r] > t:
                    l = l
                    r -= 1
            for y, z in acc:
                if (x, y, z) not in uniq:
                    ys.append([x, y, z])
                    uniq.add((x, y, z))
        return ys

