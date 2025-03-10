class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {s[0]: 1}
        C = s[0]
        l = 0
        r = 1
        acc = r - l
        while r < len(s):
            n = (r - l) - mp[C]
            if s[r] == C and n <= k:
                mp[s[r]] = mp.get(s[r], 0) + 1
                C = max(s[r], C, key=mp.__getitem__)
                r += 1
                acc = max(r - l, acc)
            elif s[r] == C and n > k:
                mp[s[l]] -= 1
                mp[s[r]] = mp.get(s[r], 0) + 1
                C = max(s[r], C, key=mp.__getitem__)
                l += 1
                r += 1
                acc = max(r - l, acc)
            elif s[r] != C and n < k:
                mp[s[r]] = mp.get(s[r], 0) + 1
                C = max(s[r], C, key=mp.__getitem__)
                r += 1
                acc = max(r - l, acc)
            elif s[r] != C and n >= k:
                mp[s[l]] -= 1
                mp[s[r]] = mp.get(s[r], 0) + 1
                C = max(s[r], C, key=mp.__getitem__)
                l += 1
                r += 1
                acc = max(r - l, acc)
        return r - l
