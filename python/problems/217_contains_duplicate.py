from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        so_far = set()
        for i in range(len(nums)):
            if nums[i] in so_far:
                return True
            so_far.add(nums[i])
        return False
