from behavioral.observer.notificationApp.IObserver import IObserver


class MobileApp(IObserver):

    def notification(self,msg):
        print(f"Mobile app received msg: {msg}")