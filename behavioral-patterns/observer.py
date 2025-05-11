from dataclasses import dataclass
from abc import ABC, abstractmethod
from collections import defaultdict


class Listener(ABC):
    @abstractmethod
    def notify(self, msg: str): ...


class EventManager:
    def __init__(self, listeners: defaultdict[str, list[Listener]] = None):
        self.listeners = listeners if listeners else defaultdict(list)

    def subscribe(self, event_type: str, listener: Listener):
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: Listener):
        self.listeners[event_type].remove(listener)

    def notify_all(self, event_type: str, msg: str):
        for listener in self.listeners[event_type]:
            listener.notify(msg)


@dataclass
class Store:
    events: EventManager = EventManager()

    def item_arrived(self, item: str):
        self.events.notify_all("item-arrival", f"Item '{item}' arrived")


@dataclass
class Person(Listener):
    name: str

    def notify(self, msg: str):
        print(f"{self.name}: {msg}")


def main():
    customers = [Person("Arima"), Person("Akane")]
    store = Store()
    
    for customer in customers:
        store.events.subscribe("item-arrival", customer)

    store.item_arrived("Iphone")


if __name__ == "__main__":
    main()

    """
    Arima: Item 'Iphone' arrived
    Akane: Item 'Iphone' arrived
    """
