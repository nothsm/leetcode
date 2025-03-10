class Solution:
    def longestConsecutive(self, xs: List[int]) -> int:
        mp = {}
        acc = 0
        for x in set(xs):
            mp[x] = mp.get(x - 1, 0) + 1 + mp.get(x + 1, 0)
            mp[x - mp.get(x - 1, 0)] = mp[x]
            mp[x + mp.get(x + 1, 0)] = mp[x]
            acc = max(mp[x], acc)
        return acc