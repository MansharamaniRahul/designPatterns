from structural.composite.ArthemeticExpression import ArthemeticExpression


class Number(ArthemeticExpression):

    def evaluate(self):
        return self.number

    def __init__(self, number):
        self.number = number

