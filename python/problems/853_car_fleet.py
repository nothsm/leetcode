class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        xs = sorted(zip(position, speed), key=lambda ps: ps[0], reverse=True)
        ys = []
        for p, s in xs:
            t = (target - p) / s
            if not ys or t > ys[-1]:
                ys.append(t)
        return len(ys)

        