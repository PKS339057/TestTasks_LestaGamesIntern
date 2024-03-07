from ICircularFIFO import ICircularFIFO


class ArrayCircularFIFO(ICircularFIFO):

    def __init__(self, size):
        self.buffer = [None for _ in range(size)]
        self.size = size
        self.filled_counter = 0
        self.front_idx = 0
        self.rear_idx = -1

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.buffer[self.front_idx]

    def rear(self) -> int:
        if self.is_empty():
            return -1
        return self.buffer[self.rear_idx]

    def enqueue(self, value: object) -> bool:
        if self.is_full():
            return False
        self.rear_idx = (self.rear_idx + 1) % self.size
        self.filled_counter += 1
        self.buffer[self.rear_idx] = value
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.buffer[self.front_idx] = None
        self.front_idx = (self.front_idx + 1) % self.size
        self.filled_counter -= 1
        return True

    def is_empty(self) -> bool:
        return self.filled_counter == 0

    def is_full(self) -> bool:
        return self.filled_counter == self.size

    def print_buffer(self) -> None:
        print(self.buffer)
