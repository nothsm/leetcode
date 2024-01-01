from typing import Dict, List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ns = nums
        ids: Dict[int, int] = {}
        for i in range(len(ns)):
            ids[ns[i]] = i

        for i in range(len(ns)):
            r = target - ns[i]
            if r in ids and ids[r] != i:
                return [i, ids[r]]
        return []
        