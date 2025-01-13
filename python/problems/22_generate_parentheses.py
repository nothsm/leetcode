class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ps = []
        def gen(l, r, acc):
            if l == 0 and r == 0:
                ps.append(acc)
            else:
                if l > 0:
                    gen(l - 1, r + 1, acc + "(")
                if r > 0:
                    gen(l, r - 1, acc + ")")
        gen(n, 0, "")
        return ps