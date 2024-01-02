class MinStack:

    def __init__(self):
        self.vals = []

    def push(self, val: int) -> None:
        cur_min = self.getMin() if self.vals else val
        self.vals.append((val, min(cur_min, val)))
        

    def pop(self) -> None:
        self.vals.pop()[0]

    def top(self) -> int:
        return self.vals[-1][0]

    def getMin(self) -> int:
        return self.vals[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()