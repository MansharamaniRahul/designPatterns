from creational.factoryPattern.IOperations import IOperations
from creational.factoryPattern.transformations import transformation


class SpanishOperation(IOperations):
    def transform(self,msg):
        return transformation['spanish'][msg]