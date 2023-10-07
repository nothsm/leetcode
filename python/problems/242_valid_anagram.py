"""
242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

"""
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_chars(s) == self.count_chars(t)

    def count_chars(self, s: str):
        count: dict = dict()
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] = count[s[i]] + 1    
        return count