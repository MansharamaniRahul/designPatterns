from factoryPattern.IOperations import IOperations
from factoryPattern.transformations import transformation


class EnglishOperations(IOperations):
    def transform(self, msg):
        return transformation['english'][msg]