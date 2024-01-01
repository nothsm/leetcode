from typing import List, Dict, Tuple

def count_chars(self, s: str) -> Dict[str, int]:
    cts: Dict[str, int] = {}
    for c in s:
        if c not in cts:
            cts[c] = 0
        cts[c] = cts[c] + 1
    return cts
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = [sorted(s) for s in strs]
        ans: Dict[Tuple[str, int], List[str]] = {}
        for s in ss:
            an: Tuple[str, int] = tuple(count_chars(s).items())  # this is an immutable dict
            if an not in ans:
                ans[an] = []
            ans[an].append(s)
        return list(ans.values())
