from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self): ...


class Receiver:
    def do_something(self, a: str):
        print(f'Receiver working on: {a}')


class SimpleCommand(Command):
    def __init__(self, a: str):
        self.a = a

    def execute(self):
        print(f"SimpleCommand: {self.a}")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str):
        self.receiver = receiver
        self.a = a

    def execute(self):
        print("ComplexCommand: Calling receiver to handle")
        self.receiver.do_something(self.a)


class Invoker:
    def __init__(self):
        self.on_start: Command = None
        self.on_finish: Command = None

    def do_something(self):
        print("Invoker: Starts process...")
        self.on_start.execute()
        print("Invoker: Finishes process...")
        self.on_finish.execute()


def main():
    invoker = Invoker()
    invoker.on_start = SimpleCommand("Say Hi!")
    receiver = Receiver()
    invoker.on_finish = ComplexCommand(receiver, "Send email")
    invoker.do_something()


if __name__ == "__main__":
    main()

    """
    Invoker: Starts process...
    SimpleCommand: Say Hi!
    Invoker: Finishes process...
    ComplexCommand: Calling receiver to handle
    Receiver working on: Send email
    """