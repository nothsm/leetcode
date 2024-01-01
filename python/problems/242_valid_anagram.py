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