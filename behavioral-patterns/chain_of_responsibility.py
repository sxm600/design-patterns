from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next: 'Handler' = None):
        self.next = next

    @abstractmethod
    def handle(self, x: str) -> str:
        return self.next.handle(x) if self.next else None


class MonkeyHandler(Handler):
    def handle(self, x: str) -> str:
        return f"Monkey will eat {x}" if x == "Banana" else super().handle(x)


class DogHandler(Handler):
    def handle(self, x: str) -> str:
        return f"Dog will eat {x}" if x == "Meat" else super().handle(x)


def main(handler: Handler):
    for food in ("Banana", "Meat", "Nut"):
        print(f"Who wants {food}?")

        result = handler.handle(food)

        if not result:
            result = f"Nobody wants {food}"

        print(result)


if __name__ == "__main__":
    dog_handler = DogHandler()
    monkey_handler = MonkeyHandler(dog_handler)

    main(monkey_handler)

    '''
    Who wants Banana?
    Monkey will eat Banana
    Who wants Meat?
    Dog will eat Meat
    Who wants Nut?
    Nobody wants Nut
    '''
