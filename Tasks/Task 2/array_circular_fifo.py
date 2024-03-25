from ICircularFIFO import ICircularFIFO


class ArrayCircularFIFO(ICircularFIFO):

    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.filled_counter = 0
        self.__front_idx = 0
        self.__rear_idx = -1

    def enqueue(self, value: object) -> bool:
        if self.filled_counter == self.size:
            return False
        self.__rear_idx = (self.__rear_idx + 1) % self.size
        self.filled_counter += 1
        self.buffer[self.rear_idx] = value
        return True

    def dequeue(self) -> bool:
        if self.filled_counter == 0:
            return False
        self.buffer[self.front_idx] = None
        self.__front_idx = (self.front_idx + 1) % self.size
        self.filled_counter -= 1
        return True
