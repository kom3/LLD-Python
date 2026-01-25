"""
1. Gather requirements Functional & Non functional:
    - Plug and Play model: Can be integrated with any system like a reusable service
    - Extendible: Can add new kind of notification service in new future, example SMS, Email, Push notification, Pop up..etc
    - Flexible Notification design: Dynamically adding a new header, changing font style, color...etc
    - Store all notification/logging

2. Observe the key entities and classes.

3. Draw basic UML diagram depicting the relationships of different components.

4. Pick any 2 - 3 core components and start writing pseudo code/actual code

5. Recall the design, discuss what principles and patterns are used, how can it be further improved along with trade offs.
"""

from typing import List
from abc import ABC, abstractmethod
from datetime import datetime


# @@@ Notification
class Notification(ABC):
    @abstractmethod
    def get_content(self):
        pass


class SimpleNotification(Notification):
    def __init__(self, text):
        self.msg = text

    def get_content(self):
        return self.msg


# @@@ Notification Decorator
class NotificationDecorator(Notification):
    def __init__(self, notification: Notification):
        self._notification = notification

    def get_content(self):
        return self._notification.get_content()


class TimeStampDecorator(NotificationDecorator):
    def get_content(self):
        timestamp = datetime.now().timestamp()
        return f"<< {timestamp} :: {self._notification.get_content()}"


class SignatureDecorator(NotificationDecorator):
    def get_content(self):
        signature = "signed_by: Notification Service"
        return f"{self._notification.get_content()} :: {signature} >>"


# @@@ Notification Observer
class NotificationObserver(ABC):
    @abstractmethod
    def update(self):
        pass


# @@@ Notification Observable
class NotificationObservable(ABC):
    @abstractmethod
    def attach(self, observer: NotificationObserver):
        pass

    @abstractmethod
    def detach(self, observer: NotificationObserver):
        pass

    @abstractmethod
    def set_notification(self, notification: Notification):
        pass

    @abstractmethod
    def get_notification(self):
        pass

    @abstractmethod
    def notify(self):
        pass


# @@@ Notification Observable Concrete Class
class NotificationCenter(NotificationObservable):
    def __init__(self):
        self._observers: List[NotificationObserver] = []
        self._notification: Notification

    def attach(self, observer: NotificationObserver):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: NotificationObserver):
        self._observers.remove(observer)

    def set_notification(self, notification: Notification):
        self._notification = notification
        self.notify()

    def get_notification(self):
        return self._notification.get_content()

    def notify(self):
        for ob in self._observers:
            ob.update()


# @@@ Notification Observer Concrete Logger class
class NotificationLogger(NotificationObserver):
    def __init__(self, notification_center: NotificationCenter):
        self._notification_center = notification_center

    def update(self):
        print(f"Logging notification message: {self._notification_center.get_notification()}")


# @@@ Notification strategy abstract class
class NotificationStrategy(ABC):
    @abstractmethod
    def send_notification(self, msg: str):
        pass


# @@@ Notification Email Strategy Concrete class
class EmailNotification(NotificationStrategy):
    def __init__(self, email_id: str):
        self.email_id = email_id

    def send_notification(self, msg: str):
        print(f"Sending Email to {self.email_id} with notification message: {msg}")


# @@@ Notification SMS Strategy Concrete class
class SMSNotification(NotificationStrategy):
    def __init__(self, mobile_no: str):
        self.mobile_no = mobile_no

    def send_notification(self, msg: str):
        print(f"Sending SMS to {self.mobile_no} with notification message: {msg}")


# @@@ Notification Popup Strategy Concrete class
class PopupNotification(NotificationStrategy):
    def send_notification(self, msg: str):
        print(f"Triggering Popup with notification message: {msg}")


# @@@ Notification Engine class
class NotificationEngine(NotificationObserver):
    def __init__(self, notification_center: NotificationCenter):
        self._notification_center = notification_center
        self._notification_strategies = []

    def add_notification_strategy(self, notification_strategy: NotificationStrategy):
        self._notification_strategies.append(notification_strategy)

    def update(self):
        for ns in self._notification_strategies:
            msg = self._notification_center.get_notification()
            ns.send_notification(msg)


# @@@ Notification Service Singleton class (to store the notifications)
class NotificationService:
    _instance = None

    # Pythonic way of implementing singleton class
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._notification_list = []  # This is to maintain history(store notifications)
        self._notification_center = NotificationCenter()

    def get_notification_center(self):
        return self._notification_center

    def send_notification(self, notification: Notification):
        self._notification_list.append(notification)
        self._notification_center.set_notification(notification)


# @@@ Client code

if __name__ == "__main__":
    # Create notification service
    notification_service = NotificationService()

    # Get the notification center(observable) instance
    notification_center = notification_service.get_notification_center()

    # Create logger observer instance
    logger = NotificationLogger(notification_center)

    # Create notification engine observers(to add strategies)
    notification_engine = NotificationEngine(notification_center)

    # Create and add notification strategies
    notification_engine.add_notification_strategy(EmailNotification("manjunath@gmail.com"))
    notification_engine.add_notification_strategy(PopupNotification())
    notification_engine.add_notification_strategy(SMSNotification("+91 1112223334"))

    # attach observers
    notification_center.attach(logger)
    notification_center.attach(notification_engine)

    # create notifications
    notification1 = SimpleNotification("You got a new subscriber!")
    notification1 = TimeStampDecorator(notification1)
    notification1 = SignatureDecorator(notification1)

    notification2 = SimpleNotification("You got a new Like!")
    notification2 = TimeStampDecorator(notification2)
    notification2 = SignatureDecorator(notification2)

    notifications = [notification1, notification2]
    for nt in notifications:
        notification_service.send_notification(nt)


