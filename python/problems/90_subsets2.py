class Solution:
    def subsetsWithDup(self, xs: List[int]) -> List[List[int]]:
        xs = sorted(xs)

        accs = set()
        def go(xs, acc):
            match xs:
                case []:
                    accs.add(tuple(acc))
                case [x, *xs]:
                    go(xs, acc)
                    acc.append(x)
                    go(xs, acc)
                    acc.pop()

        go(xs, [])
        return [list(xs) for xs in accs]