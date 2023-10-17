from typing import List

"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1) 
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets: List[List[int]] = list()

        nums = sorted(nums)
        for i in range(len(nums)):
            target: int = -nums[i]
            left: int = i + 1
            right: int = len(nums) - 1
            
            while left < right:
                s: int = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    triplet: List[int] = [nums[i], nums[left], nums[right]]
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == triplet[1]:
                        left += 1
                    while left < right and nums[right] == triplet[2]:
                        right -= 1
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
        return triplets