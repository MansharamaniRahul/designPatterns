from behavioral.strategy.VehicleStrategy import VehicleStrategy


class SportsDriveStrategy(VehicleStrategy):

    def drive(self):
        print("Sport drive mode activated")