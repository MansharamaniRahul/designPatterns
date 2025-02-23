from factoryPattern.FrenchOperation import FrenchOperation
from factoryPattern.ILocalizationFactory import ILocalizationFactory

class FrenchFactory(ILocalizationFactory):
    def get_localizer(self):
        return FrenchOperation()