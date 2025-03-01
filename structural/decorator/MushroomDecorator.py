from structural.decorator.BasePizza import BasePizza
from structural.decorator.ToppingsDecorator import ToppingsDecorator


class MushroomDecorator(ToppingsDecorator):

    def __init__(self, basePizza):
        self.basePizza= basePizza

    def cost(self):
        self.basePizza.cost()+30