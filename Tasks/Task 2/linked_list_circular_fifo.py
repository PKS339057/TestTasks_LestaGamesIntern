from ICircularFIFO import ICircularFIFO


class Node:
    def __init__(self, val, nxt=None, is_front=False, is_rear=False):
        self.val = val
        self.nxt = nxt
        self.is_front = is_front
        self.is_rear = is_rear


class LinkedListCircularFIFO(ICircularFIFO):
    def __init__(self, size):
        self.size = size
        self.filled_counter = 0
        self.front_node = None
        self.rear_node = None
        self.__set_nodes()

    def __set_nodes(self):
        first_node = Node(None)
        self.front_node = first_node
        self.rear_node = self.front_node
        nodes = first_node
        for _ in range(self.size - 2):
            nodes.nxt = Node(None)
            nodes = nodes.nxt
        nodes.nxt = Node(None, nxt=first_node)

    def front(self) -> int:
        if self.is_empty():
            return -1
        return self.front_node.val

    def rear(self) -> int:
        if self.is_empty():
            return -1
        return self.rear_node.val

    def enqueue(self, value: object) -> bool:
        if self.is_full():
            return False
        if not(self.is_empty()):
            self.rear_node = self.rear_node.nxt
        self.rear_node.val = value
        self.filled_counter += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.front_node.val = None
        if self.filled_counter > 1:
            self.front_node = self.front_node.nxt
        self.filled_counter -= 1
        return True

    def is_empty(self) -> bool:
        return self.filled_counter == 0

    def is_full(self) -> bool:
        return self.filled_counter == self.size

    def print_buffer(self) -> None:
        result = []
        cur_node = self.front_node
        for _ in range(self.filled_counter):
            result.append(cur_node.val)
            cur_node = cur_node.nxt
        print(result)
