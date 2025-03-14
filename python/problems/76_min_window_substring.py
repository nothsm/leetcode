def frequencies(xs):
    mp = {}
    for x in xs:
        mp[x] = mp.get(x, 0) + 1
    return mp

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        fs = frequencies(t)
        rem = len(t)
        acc = s + "x"
        while r < len(s) or rem == 0:
            if rem == 0 and s[l] in fs and fs[s[l]] >= 0:
                acc = min(acc, s[l:r], key=len)
                fs[s[l]] += 1
                rem += 1
                l += 1
            elif rem == 0 and s[l] in fs and fs[s[l]] < 0:
                acc = min(acc, s[l:r], key=len)
                fs[s[l]] += 1
                l += 1
            elif rem == 0 and s[l] not in fs:
                acc = min(acc, s[l:r], key=len)
                l += 1
            elif rem > 0 and s[r] in fs and fs[s[r]] > 0:
                fs[s[r]] -= 1
                rem -= 1
                r += 1
            elif rem > 0 and s[r] in fs and fs[s[r]] <= 0:
                fs[s[r]] -= 1
                r += 1
            elif rem > 0 and s[r] not in fs:
                r += 1
        return acc if acc != s + "x" else ""