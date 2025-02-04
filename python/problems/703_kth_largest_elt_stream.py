import heapq

class KthLargest:

    def __init__(self, k: int, xs: List[int]):
        self.xs = []
        for x in sorted(xs, reverse=True)[:k]:
            heapq.heappush(self.xs, x)
        self.k = k



    def add(self, v: int) -> int:

        if len(self.xs) < self.k:
            heapq.heappush(self.xs, v)
        elif v > self.xs[0]:
            heapq.heappop(self.xs)
            heapq.heappush(self.xs, v)
        
        return self.xs[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)