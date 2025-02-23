class NotificationService:

    def __init__(self):
        self.observers=set()

    def add(self,observer):
        self.observers.add(observer)

    def remove(self,observer):
        self.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.notification(msg)