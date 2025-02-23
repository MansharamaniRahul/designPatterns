from creational.factoryPattern.ILocalizationFactory import ILocalizationFactory
from creational.factoryPattern.EnglishOperations import EnglishOperations

class EnglishFactory(ILocalizationFactory):
    def get_localizer(self):
        return EnglishOperations()
