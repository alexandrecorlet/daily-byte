from collections import deque


class StackQueue:
    
    def __init__(self, size):
        self.size = size
        self.queue = deque()

    # O(n)
    def push(self, data):
        if len(self.queue) >= self.size:
            raise IndexError("Stack Overflow")

        # Enqueue the new data
        self.queue.append(data)
        
        # Remove and reinsert all data in 
        # front of the new data so the new data becomes the head of the queue
        while self.peek() != data:
            self.queue.append(self.queue.popleft())

    # O(1)
    def pop(self):
        if self.empty():
            raise IndexError("Stack is empty")
        return self.queue.popleft()

    # O(1)
    def peek(self):
        if self.empty():
            raise IndexError("Stack is empty")
        return self.queue[0]
    
    # O(1)
    def empty(self):
        return len(self.queue) == 0


def main():
    stack = StackQueue(3)
    assert stack.empty()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.empty()

if __name__ == "__main__":
    main()



