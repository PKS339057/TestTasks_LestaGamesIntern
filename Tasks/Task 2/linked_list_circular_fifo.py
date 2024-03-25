from ICircularFIFO import ICircularFIFO


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


class LinkedListCircularFIFO(ICircularFIFO):
    def __init__(self, size):
        self.size = size
        self.filled_counter = 0
        self.front_node = None
        self.rear_node = None

        # Создание связного списка в памяти
        first_node = Node(None)
        self.front_node = first_node
        self.rear_node = self.front_node
        nodes = first_node
        for _ in range(self.size - 2):
            nodes.nxt = Node(None)
            nodes = nodes.nxt
        nodes.nxt = Node(None, nxt=first_node)

    def enqueue(self, value: object) -> bool:
        if self.is_full():
            return False
        if not(self.is_empty()):
            self.rear_node = self.rear_node.nxt
        self.rear_node.val = value
        self.filled_counter += 1
        return True

    def dequeue(self) -> bool:
        if self.filled_counter == 0:
            return False
        self.front_node.val = None
        if self.filled_counter > 1:
            self.front_node = self.front_node.nxt
        self.filled_counter -= 1
        return True
