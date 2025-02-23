from creational.factoryPattern.FrenchOperation import FrenchOperation
from creational.factoryPattern.ILocalizationFactory import ILocalizationFactory

class FrenchFactory(ILocalizationFactory):
    def get_localizer(self):
        return FrenchOperation()