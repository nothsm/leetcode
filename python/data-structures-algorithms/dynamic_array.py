"""
Design Dynamic Array (Resizable Array)
Design a Dynamic Array class, similar to an ArrayList in Java or vector in C++.

DynamicArray class should support the following:
1. DynamicArray(int capacity): Initialize array with a capacity of 'capacity'.
2. int get(int i): Return element at index 'i'. Assume 'i' is valid.
3. void insert(int i, int n): Insert element 'n' at index 'i'. Assume 'i' is
   valid.
4. void pushback(int n): Push element 'n' to the end of the array.
5. int popback(): Pop and return element at the end. Assume array is non-empty.
6. void resize(): Double the capacity.
7. int getSize(): Return the number of elements.
8. int getCapacity(): Return the capacity.

Constraints:
- If 'void pushback(int n)' is called but array is full, resize array first.

Examples:
Example 1:
Input: ["Array", 1, "getSize", "getCapacity"]
Output: [null, 0, 1]

Example 2:
Input: ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
Output: [null, null, 1, null, 2]

Note:
- 'i' for 'get(int i)' and 'insert(int i)' is >= 0 and < number of elements.
"""


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
