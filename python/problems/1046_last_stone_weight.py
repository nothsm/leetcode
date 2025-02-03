import heapq

class Solution:
    def lastStoneWeight(self, xs: List[int]) -> int:

        q = []
        for x in xs:
            heapq.heappush(q, -x)


        def go(xs):
            match xs:
                case []:
                    return 0
                case [x]:
                    return -x
                case _:
                    y = heapq.heappop(xs); y = -y
                    x = heapq.heappop(xs); x = -x
                    if x != y:
                        heapq.heappush(xs, -(y - x))
                    return go(xs)
        return go(q)
