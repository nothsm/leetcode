def frequencies(s):
    mp = {}
    for c in s:
        mp[c] = mp.get(c, 0) + 1
    return mp


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fs = frequencies(s1)
        rem = len(s1)
        l = 0
        r = 0
        while r < len(s2):
            if r - l + 1 < len(s1):
                if s2[r] in fs:
                    fs[s2[r]] -= 1
                    if fs[s2[r]] >= 0:
                        rem -= 1
                r += 1
                if rem <= 0: return True
            else:
                if s2[r] in fs:
                    fs[s2[r]] -= 1
                    if fs[s2[r]] >= 0:
                        rem -= 1
                r += 1
                if rem <= 0: return True
                if s2[l] in fs:
                    fs[s2[l]] += 1
                    if fs[s2[l]] > 0:
                        rem += 1
                l += 1
            if rem <= 0: return True
        return False
        