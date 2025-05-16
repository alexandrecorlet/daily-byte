from collections import deque


class MovingAverage:
    
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val):
        self.sum += val
        if len(self.queue) >= self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        return self.sum / len(self.queue)


def main():
    
    ma = MovingAverage(3)

    print(ma.next(3))
    print(ma.next(5))
    print(ma.next(7))
    print(ma.next(6))


if __name__ == "__main__":
    main()

