class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ids, l, max_len = {}, 0, 0
        for r in range(len(s)):
            next_in_window: bool = s[r] in ids and l <= ids[s[r]]
            if next_in_window:
                l = ids[s[r]] + 1
            max_len = max(max_len, (r - l) + 1)
            ids[s[r]] = r
        return max_len
