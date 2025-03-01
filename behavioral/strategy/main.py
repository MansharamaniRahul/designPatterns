from behavioral.strategy.NormalHatchBackVehicle import NormalHatchBackVehicle
from behavioral.strategy.SportsVehicle import SportsVehicle


def main():
    sportsVehicle=SportsVehicle()
    sportsVehicle.drive()

    normalVehicle=NormalHatchBackVehicle()
    normalVehicle.drive()

if __name__== "__main__":
    main()