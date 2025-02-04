class Solution:
    def permute(self, xs: List[int]) -> List[List[int]]:
        accs = []
        def go(xs, acc):
            match xs:
                case []:
                    accs.append(list(acc))
                case _:
                    for i in range(len(xs)):
                        x = xs.pop(i)
                        acc.append(x)
                        go(xs, acc)
                        acc.pop()
                        xs.insert(i, x)
                        

        go(xs, [])
        return accs

