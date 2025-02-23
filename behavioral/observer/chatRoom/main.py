from behavioral.observer.chatRoom.ChatRoom import ChatRoom
from behavioral.observer.chatRoom.Participant import Participant


def main():
    chatRoom = ChatRoom()
    participant1= Participant("participant1")
    participant2 = Participant("participant2")
    participant3 = Participant("participant3")
    chatRoom.join(participant1)
    chatRoom.join(participant2)
    chatRoom.join(participant3)
    chatRoom.join(participant3)
    chatRoom.broadcast("Msg broadcasting successfull !! ")

if __name__== "__main__":
    main()
