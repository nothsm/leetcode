class Solution:
    def searchMatrix(self, xss: List[List[int]], t: int) -> bool:
        def idxs(i):
            return i // len(xss[0]), i % len(xss[0])

        def go(l, r):
            il, jl = idxs(l)
            ir, jr = idxs(r)
            
            xl = xss[il][jl]
            xr = xss[ir][jr]

            im, jm = idxs((l + r) // 2)
            xm = xss[im][jm]
            if xl == t:
                return True
            elif xr == t:
                return True
            elif r - l - 1 == 0:
                return False
            elif t <= xm:
                return go(l, (l + r) // 2)
            else:
                return go((l + r) // 2, r)

        match xss:
            case []:
                return False
            case [[x]]:
                return x == t
            case _:
                return go(0, len(xss) * len(xss[0]) - 1)