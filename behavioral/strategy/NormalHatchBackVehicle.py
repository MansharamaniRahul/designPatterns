from behavioral.strategy.NormalDriveStrategy import NormalDriveStrategy
from behavioral.strategy.Vehicle import Vehicle


class NormalHatchBackVehicle(Vehicle):
    
    def __init__(self):
        super().__init__(NormalDriveStrategy())