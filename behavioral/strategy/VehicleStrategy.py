from abc import abstractmethod, ABC


class VehicleStrategy(ABC):

    @abstractmethod
    def drive(self):
        pass