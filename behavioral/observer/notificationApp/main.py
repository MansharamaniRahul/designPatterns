from behavioral.observer.notificationApp.MobileApp import MobileApp
from behavioral.observer.notificationApp.NotificationServerice import NotificationService
from behavioral.observer.notificationApp.WebApp import WebApp


def main():
    notificationService= NotificationService()
    webApp= WebApp()
    mobileApp= MobileApp()
    notificationService.add(webApp)
    notificationService.add(mobileApp)
    notificationService.notify("Testing notifications!!")

if __name__ == "__main__":
    main()
