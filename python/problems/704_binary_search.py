class Solution:
    def search(self, xs: List[int], target: int) -> int:
        lo = 0
        hi = len(xs) - 1
        mid = ((hi - lo) // 2) + lo
        while xs[lo] != target and xs[mid] != target and xs[hi] != target:
            if lo >= mid or mid >= hi or lo >= hi:
                break
            if target < xs[mid]:
                hi = mid
                mid = ((hi - lo) // 2) + lo
            elif target > xs[mid]:
                lo = mid
                mid = ((hi - lo) // 2) + lo
            
        if xs[lo] == target:
            return lo
        elif xs[mid] == target:
            return mid
        elif xs[hi] == target:
            return hi
        else:
            return -1