from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def notification(self, msg):
        pass