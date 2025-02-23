from factoryPattern.ILocalizationFactory import ILocalizationFactory
from factoryPattern.EnglishOperations import EnglishOperations

class EnglishFactory(ILocalizationFactory):
    def get_localizer(self):
        return EnglishOperations()
