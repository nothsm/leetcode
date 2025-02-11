class Solution:
    def combinationSum(self, xs: List[int], t: int) -> List[List[int]]:
        accs = set()

        def go(s, acc):
            if s > t:
                return
            elif s == t:
                accs.add(tuple(acc))
            else:
                for x in xs:
                    if acc == [] or acc[-1] <= x:
                        acc.append(x)
                        go(s + x, acc)
                        acc.pop()

        go(0, [])
        return [list(acc) for acc in accs]