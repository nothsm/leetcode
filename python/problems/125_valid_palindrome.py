"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters to
lowercase and removing all non-alphanumeric characters, it reads the same
forward and backward.

Given a string s, return True if it is a palindrome, or False otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

"""
Time complexity: O(n)
Space complexity: O(n)
"""

def clean_str(self, s: str) -> str:
    clean = ""
    for c in s:
        if c.isalnum():
            clean += c
    return clean

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = clean_str(s.lower())
        left = 0
        right = len(clean) - 1
        while left < right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        return True
    
