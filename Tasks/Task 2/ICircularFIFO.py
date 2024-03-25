from abc import ABC, abstractmethod


class ICircularFIFO(ABC):
    @abstractmethod
    def enqueue(self, value: object) -> bool:
        pass

    @abstractmethod
    def dequeue(self) -> bool:
        pass
