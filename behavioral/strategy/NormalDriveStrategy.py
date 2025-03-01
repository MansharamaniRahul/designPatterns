from behavioral.strategy.VehicleStrategy import VehicleStrategy


class NormalDriveStrategy(VehicleStrategy):

    def drive(self):
        print("Normal driving mode activated")