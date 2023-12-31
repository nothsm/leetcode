from typing import List

def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for x in nums:
            if x != val:
                nums[left] = x
                left += 1
        return left