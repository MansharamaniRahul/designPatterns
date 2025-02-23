from factoryPattern.ILocalizationFactory import  ILocalizationFactory
from factoryPattern.SpanishOperation import SpanishOperation


class SpanishFactory(ILocalizationFactory):
    def get_localizer(self):
        return SpanishOperation()