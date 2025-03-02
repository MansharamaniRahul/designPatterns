from structural.composite.Expression import Expression
from structural.composite.Number import Number


def main():
    one = Number(1)
    two=Number(2)
    seven=Number(7)
    addExpression =Expression(one,seven,"ADD")
    parentExpression=Expression(two,addExpression,"MUL")
    print(f"Value is {parentExpression.evaluate()}")

if __name__ =="__main__":
    main()