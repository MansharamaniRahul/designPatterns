from structural.composite.ArthemeticExpression import ArthemeticExpression


class Expression(ArthemeticExpression):

    def __init__(self, leftExpression, rightExpression, operation):
        self.leftExpression= leftExpression
        self.rightExpression=rightExpression
        self.operation=operation

    def evaluate(self):
        value=0

        match self.operation:
            case "ADD":
                return self.leftExpression.evaluate() + self.rightExpression.evaluate()
            case "SUB":
                return self.leftExpression.evaluate() -self.rightExpression.evaluate()
            case "MUL":
                return self.leftExpression.evaluate() * self.rightExpression.evaluate()
            case "DIVIDE":
                return self.leftExpression.evaluate() /self.rightExpression.evaluate()
