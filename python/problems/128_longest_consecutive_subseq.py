def dedup(xs):
    ys = []
    seen = set()
    for x in xs:
        if x not in seen:
            ys.append(x)
            seen.add(x)
    return ys


class Solution:
    def longestConsecutive(self, xs: List[int]) -> int:
        xs = dedup(xs)
        ys = set(xs)

        acc = 0
        for x in xs:
            if x - 1 not in ys:
                seq = 0
                y = x
                while y in ys:
                    seq += 1
                    y += 1
                acc = max(seq, acc)
        return acc
        