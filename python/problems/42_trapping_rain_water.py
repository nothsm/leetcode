from itertools import accumulate
from typing import List

"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

def rev(obj):
    return reversed(obj)

def acc(obj, f):
    return accumulate(obj, func=f)

class Solution:
    def trap(self, height: List[int]) -> int:
        hs = height
        lms: List[int] = list(acc(hs, f=max))
        rms: List[int] = list(rev(list(acc(rev(hs), f=max))))
        w: int = 0
        for i in range(len(hs)):
            w += min(lms[i], rms[i]) - hs[i]
        return w