from typing import List

class DoubleEndedQueue:
    def __init__(self):
        self.front: Node = None
        self.back: Node = None
        self.size: int = 0

    def push_front(self, element) -> None:
        # TODO: Add an element to the front of the deque.
        if self.is_empty():
            self.front = Node(element, None, None)
            self.back = self.front
        else:
            self.front.prev = Node(element, self.front, None)
            self.front = self.front.prev
        self.size += 1

    def push_back(self, element) -> None:
        # TODO: Add an element to the back of the deque.
        if self.is_empty():
            self.back = Node(element, None, None)
            self.front = self.back
        else:
            self.back.next = Node(element, None, self.back)
            self.back = self.back.next
        self.size += 1
    
    def pop_front(self) -> int:
        # TODO: Remove and return the element from the front.
        # Return None if the deque is empty.
        out: int = None
        if not self.is_empty():
            out = self.front.value
            if self.size == 1:
                self.front = None
                self.back = None
            else:
                self.front = self.front.next
                self.front.prev = None
            self.size -= 1
        return out
    
    def pop_back(self) -> int:
        # TODO: Remove and return the element from the back.
        # Return None if the deque is empty.
        out: int = None
        if not self.is_empty():
            out = self.back.value
            if self.size == 1:
                self.front = None
                self.back = None
            else:
                prev: Node = self.back.prev
                prev.next = None
                self.back = prev
            self.size -= 1
        return out

    
    def peek_front(self) -> int:
        # TODO: View the element at the front without removing it.
        # Return None if the deque is empty.
        out: int = None
        if not self.is_empty():
            out = self.front.value
        return out
    
    def peek_back(self) -> int:
        # TODO: View the element at the back without removing it.
        # Return None if the deque is empty.
        out: int = None
        if not self.is_empty():
            out = self.back.value
        return out
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def get_size(self) -> int:
        return self.size
    
    def get_values(self) -> List[int]:
        out: List = []
        current: Node = self.front
        while current != None:
            out.append(current.value)
            current = current.next
        return out
    
    def __str__(self) -> str:
        return str(self.get_values())

class Node:
    def __init__(self, value: int = 0, next: 'Node' = None, prev: 'Node' = None):
        self.value = value
        self.next = next
        self.prev = prev


def test_my_deque():
    # Initialize deque
    dq = DoubleEndedQueue()
    
    # Test is_empty on an empty deque
    assert dq.is_empty() == True
    
    # Test push and pop front
    dq.push_front(1)
    assert dq.pop_front() == 1
    
    # Test push and pop back
    dq.push_back(2)
    assert dq.pop_back() == 2
    
    # Test peek front and back on empty deque
    assert dq.peek_front() is None
    assert dq.peek_back() is None
    
    # More complex scenarios
    dq.push_front(1)
    dq.push_back(2)
    dq.push_back(3)
    dq.push_front(0)
    
    assert dq.pop_front() == 0
    assert dq.pop_back() == 3
    
    # Test size
    assert dq.get_size() == 2

def test_initialization():
    dq = DoubleEndedQueue()
    assert dq.is_empty() == True
    assert dq.get_size() == 0

def test_basic_operations():
    dq = DoubleEndedQueue()
    
    # Test push_front and pop_front
    dq.push_front(1)
    assert dq.pop_front() == 1
    
    # Test push_back and pop_back
    dq.push_back(2)
    assert dq.pop_back() == 2

def test_boundary_cases():
    dq = DoubleEndedQueue()
    
    # Test pop and peek on empty deque
    assert dq.pop_front() is None
    assert dq.pop_back() is None


def main():
    test_my_deque()
    test_initialization()
    test_basic_operations()
    test_boundary_cases()

if __name__ == '__main__':
    main()
