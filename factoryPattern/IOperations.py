from abc import abstractmethod, ABC


class IOperations(ABC):
    @abstractmethod
    def transform(self, msg):
        pass