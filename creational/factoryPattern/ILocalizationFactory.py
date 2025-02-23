from abc import ABC, abstractmethod

class ILocalizationFactory(ABC):
    @abstractmethod
    def get_localizer(self):
        pass