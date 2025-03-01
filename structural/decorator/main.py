from structural.decorator.CheesPizza import CheesPizza
from structural.decorator.MushroomDecorator import MushroomDecorator


def main():
    chessPizza= CheesPizza()
    mushroomDecorator=MushroomDecorator(chessPizza)
    print(f"Cost of Chees pizza with mushroom toppings is {mushroomDecorator.cost()}")


if __name__ == "__main__":
    main()