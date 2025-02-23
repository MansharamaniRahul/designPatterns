from behavioral.observer.notificationApp.IObserver import IObserver


class WebApp(IObserver):

    def notification(self, msg):
        print(f"Web App received msg: {msg}")