"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest  substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

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
