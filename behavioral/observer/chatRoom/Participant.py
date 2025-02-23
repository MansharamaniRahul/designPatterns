from behavioral.observer.chatRoom.IParticipants import IParticipants


class Participant(IParticipants):

    def __init__(self, name):
        self.name= name


    def receive_message(self, msg):
        print(f"{self.name}-->message received: {msg}")