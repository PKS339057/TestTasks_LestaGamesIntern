from abc import ABC, abstractmethod


class ICircularFIFO(ABC):
    @abstractmethod
    def enqueue(self, value: object) -> bool:
        pass

    @abstractmethod
    def dequeue(self) -> bool:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def print_buffer(self) -> None:
        pass
