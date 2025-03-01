from behavioral.strategy.SportsDriveStrategy import SportsDriveStrategy
from behavioral.strategy.Vehicle import Vehicle


class SportsVehicle(Vehicle):

    def __init__(self):
        super().__init__(SportsDriveStrategy())
