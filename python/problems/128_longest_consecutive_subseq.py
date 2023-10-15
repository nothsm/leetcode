from typing import Dict, List

"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Example 2: 
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

"""
Time complexity: O(n)
Space Complexity: O(n) 
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs: Dict[int, int] = dict()
        longest: int = 0

        for n in nums:
            if n not in seqs:
                l: int = seqs.get(n-1, 0)
                r: int= seqs.get(n+1, 0)
                seq_len: int = l + r + 1
                
                seqs[n] = seq_len
                longest = max(seq_len, longest)
                seqs[n-l] = seq_len
                seqs[n+r] = seq_len
        return longest