class Solution:
    def subsets(self, xs: List[int]) -> List[List[int]]:
        accs = []
        def go(xs, acc):
            match xs:
                case []:
                    accs.append(list(acc))
                case [x, *xs]:
                    go(xs, acc) # dont choose
                    acc.append(x); go(xs, acc); acc.pop() # choose
        go(xs, [])
        return accs
                    