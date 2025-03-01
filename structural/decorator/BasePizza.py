from abc import abstractmethod, ABC


class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass