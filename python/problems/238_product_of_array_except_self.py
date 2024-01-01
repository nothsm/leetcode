from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left: List[int] = [1] * len(nums)
        right: int = 1
        out: List[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            out[i] = left[i] * right
            right *= nums[i]
        return out
