class ChatRoom():
    def __init__(self):
        self.participants=set()

    def join(self,participant):
        self.participants.add(participant)

    def leave(self,participant):
        self.participants.remove(participant)

    def broadcast(self, msg):
        for participant in self.participants:
            participant.receive_message(msg)
