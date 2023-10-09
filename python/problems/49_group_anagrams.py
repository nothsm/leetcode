from typing import List, Dict, Tuple

"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, typically using all the original letters exactly
once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

"""
Time complexity = O(n * m * log(m))
Space complexity = O(n)
  n = # of given strings
  m = max length of any given string
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[Tuple[str, int], List[str]] = {}
        for s in strs:
            anagram: Tuple[str, int] = tuple(self.count_chars(sorted(s)).items())
            if anagram not in anagrams:
                anagrams[anagram] = []
            anagrams[anagram].append(s)
        return list(anagrams.values())

    def count_chars(self, s: str) -> Dict[str, int]:
        count: Dict[str, int] = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] = count[s[i]] + 1
        return count
