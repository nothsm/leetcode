class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        mp = {}
        acc = 0
        while r < len(s):
            if mp.get(s[r], 0) == 0:
                mp[s[r]] = 1
                r += 1
                acc = max(acc, r - l)
            else:
                mp[s[l]] -= 1
                l += 1
        return acc