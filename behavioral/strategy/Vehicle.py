from abc import abstractmethod, ABC

from behavioral.strategy.VehicleStrategy import VehicleStrategy


class Vehicle(ABC):

    def __init__(self, strategy: VehicleStrategy):
        self.strategy= strategy

    def drive(self):
        self.strategy.drive()


