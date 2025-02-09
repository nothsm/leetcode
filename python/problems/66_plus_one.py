class Solution:
    def plusOne(self, xs: List[int]) -> List[int]:
        def go(xs, acc):
            match xs:
                case []:
                    return list(reversed(acc))
                case [x] if x >= 10 :
                    xs.append(0)
                    return go(xs, acc)
                case [x, *xs] if x >= 10:
                    acc.append(x % 10)
                    xs[0] += 1
                    return go(xs, acc)
                case [x, *xs]:
                    acc.append(x)
                    return go(xs, acc)

        xs[-1] += 1
        return go(list(reversed(xs)), [])
        