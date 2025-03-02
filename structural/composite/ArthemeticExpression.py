from abc import abstractmethod, ABC


class ArthemeticExpression(ABC):

    @abstractmethod
    def evaluate(self):
        pass