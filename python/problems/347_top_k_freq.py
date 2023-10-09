from typing import List, Dict, Optional

'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''

'''
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''

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