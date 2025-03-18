class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ps = set()
        def go(l, r, acc):
            if l == 0 and r == 0:
                ps.add(acc)
            elif l == 0:
                go(l, r - 1, acc + ")")
            elif l < r:
                go(l - 1, r, acc + "(")
                go(l, r - 1, acc + ")")
            elif r >= l:
                go(l - 1, r, acc + "(")
        go(n, n, "")
        return list(ps)
        