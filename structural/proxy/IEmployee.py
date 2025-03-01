from abc import abstractmethod, ABC


class IEmployee(ABC):

    @abstractmethod
    def create(self, role,childDetails, childObj ):
        pass