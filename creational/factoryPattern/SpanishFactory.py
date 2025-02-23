from creational.factoryPattern.ILocalizationFactory import  ILocalizationFactory
from creational.factoryPattern.SpanishOperation import SpanishOperation


class SpanishFactory(ILocalizationFactory):
    def get_localizer(self):
        return SpanishOperation()