from factoryPattern.IOperations import IOperations
from factoryPattern.transformations import transformation


class SpanishOperation(IOperations):
    def transform(self,msg):
        return transformation['spanish'][msg]