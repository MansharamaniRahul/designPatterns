from creational.factoryPattern.IOperations import IOperations
from creational.factoryPattern.transformations import transformation


class EnglishOperations(IOperations):
    def transform(self, msg):
        return transformation['english'][msg]