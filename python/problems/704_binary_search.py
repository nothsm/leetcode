class Solution:
    def search(self, xs: List[int], t: int) -> int:
        def go(l, r):
            if xs[l] == t:
                return l
            elif xs[r] == t:
                return r
            elif r - l - 1 == 0: # window size = r - l - 1
                return -1
            elif t <= xs[(l + r) // 2]:
                return go(l, (l + r) // 2)
            else:
                return go((l + r) // 2, r)
        match xs:
            case []:
                return -1
            case [x]:
                return 0 if x == t else -1
            case _:
                return go(0, len(xs) - 1)