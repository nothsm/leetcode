"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

def counts(s: str) -> Dict[str, int]:
    cs = {}
    for c in s: 
        cs[c] = cs.get(c, 0) + 1
    return cs 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        counts1 = counts(s1)
        counts2 = counts(s2[0: len(s1) - 1])
        for c in s2[len(s1)-1:]:
            counts2[c] = counts2.get(c , 0) + 1
            if counts1 == counts2: 
                return True
            counts2[s2[left]] -= 1
            if counts2[s2[left]] == 0: 
                del counts2[s2[left]]
            left += 1
        return False