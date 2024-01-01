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
    
