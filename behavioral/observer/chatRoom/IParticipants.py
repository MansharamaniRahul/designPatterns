from abc import abstractmethod, ABC


class IParticipants(ABC):

    @abstractmethod
    def receive_message(self, msg):
        pass