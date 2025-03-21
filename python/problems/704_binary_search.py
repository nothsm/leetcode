class Solution:
    def search(self, xs: List[int], t: int) -> int:
        match xs:
            case []:
                return -1
            case [x]:
                return 0 if x == t else -1
            case [x, y]:
                if x == t:
                    return 0
                elif y == t:
                    return 1
                else:
                    return -1
            case _:
                l = 0
                r = len(xs) - 1
                while r - l > 1:
                    m = (r + l) // 2
                    if xs[l] == t:
                        return l
                    elif xs[m] == t:
                        return m
                    elif xs[r] == t:
                        return r
                    elif t < xs[m]:
                        r = m
                    elif xs[m] < t:
                        l = m
                return -1
        
