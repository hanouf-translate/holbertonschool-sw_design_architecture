#!/usr/bin/env python3
from typing import Any, Dict, Optional, Protocol, Set


class Observer(Protocol):
    def update(self, topic: str, data: Any) -> None:
        ...


class NewsSubject:
    def __init__(self) -> None:
        self._subscribers: Dict[Observer, Optional[Set[str]]] = {}

    def subscribe(
        self, observer: Observer, topics: Optional[Set[str]] = None
    ) -> None:
        self._subscribers[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        self._subscribers.pop(observer, None)

    def notify(self, topic: str, data: Any) -> None:
        for observer, topics in list(self._subscribers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic: str, data: Any) -> None:
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic: str, data: Any) -> None:
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic: str, data: Any) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    subject = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(log_observer, topics={"sports", "breaking"})
    subject.subscribe(email_observer, topics=None)
    subject.subscribe(sms_observer, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()