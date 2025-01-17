class Solution:
    def twoSum(self, xs: List[int], t: int) -> List[int]:
        l = 0
        r = len(xs) - 1
        while xs[l] + xs[r] != t:
            if xs[l] + xs[r] < t:
                l += 1
                r = r
            elif xs[l] + xs[r] > t:
                l = l
                r -= 1
        return [l + 1, r + 1]
        