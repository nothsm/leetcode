from typing import List, Dict, Optional

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: Dict[int, int] = self.count_frequencies(nums)
        vals: List[int] = sorted(list(freq.values()))
        top_k: List[int] = []
        while k > 0:  # pop the top k highest freq from vals
            key: int = self.key(vals.pop(), freq)
            top_k.append(key)
            del freq[key]
            k -= 1
        return top_k
    
    def count_frequencies(self, nums: List[int]) -> Dict[int, int]:
        freq: Dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] = freq[nums[i]] + 1
        return freq

    def key(self, value: int, dictionary: Dict[int, int]) -> Optional[int]:
        for k, v in dictionary.items():
            if v == value:
                return k
        return None