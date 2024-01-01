from typing import Dict

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