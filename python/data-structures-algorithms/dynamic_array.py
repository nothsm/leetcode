class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.array: list = [0] * capacity
        self.size: int = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def insert(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self._checkResize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        resized: list = [0] * 2 * self.capacity
        for i in range(self.capacity):
            resized[i] = self.array[i]
        self.array = resized
        self.capacity = 2 * self.capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def _checkResize(self) -> None:
        if self.size == self.capacity:
            self.resize()


def main():
    dynamic_array = DynamicArray(10)
    dynamic_array.resize()


if __name__ == "__main__":
    main()
