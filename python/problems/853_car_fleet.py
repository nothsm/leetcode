class Solution:
    def carFleet(self, T: int, ps: List[int], ss: List[int]) -> int:
        xs = sorted(zip(ps, ss), key=lambda x: x[0], reverse=True)
        acc = []
        for p, s in xs:
            t = (T - p) / s
            if not acc or acc[-1] < t:
                acc.append(t)
        return len(acc)