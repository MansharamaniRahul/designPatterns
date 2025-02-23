from factoryPattern.IOperations import IOperations
from factoryPattern.transformations import transformation


class FrenchOperation(IOperations):
    def transform(self,msg):
        return transformation['french'][msg]