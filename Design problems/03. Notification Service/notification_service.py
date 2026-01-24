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

from abc import ABC, abstractmethod
from datetime import datetime


class Notification(ABC):
    @abstractmethod
    def get_content(self):
        pass


class SimpleNotification(Notification):
    def __init__(self, text):
        self.msg = text

    def get_content(self):
        return self.msg


class NotificationDecorator(Notification):
    def __init__(self, notification: Notification):
        self._notification = notification

    def get_content(self):
        return self._notification.get_content()


class TimeStampDecorator(NotificationDecorator):
    def get_content(self):
        timestamp = datetime.now().timestamp()
        return f"{timestamp} | {self._notification.get_content()}"
    
class SignatureDecorator(NotificationDecorator):
    def get_content(self):
        signature = "signed_by: Manjunath"
        return f"{self._notification.get_content()} | {signature}"
    
class NotificationObservable(ABC):
    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass
    @abstractmethod
    def set_notification(self):
        pass

    @abstractmethod
    def get_notification(self):
        pass

    @abstractmethod
    def notify(self):
        pass