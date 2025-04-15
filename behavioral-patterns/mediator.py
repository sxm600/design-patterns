from abc import ABC, abstractmethod


class IMediator(ABC):
    @abstractmethod
    def notify(self, sender: "BaseForce", event: str): ...


class Station(IMediator):
    def __init__(self):
        self.forces: list["BaseForce"] = []

    def notify(self, sender: "BaseForce", event: str):
        if event == "A":
            print(f"Mediator: {sender} does A")

            for force in self.forces:
                if force != sender:
                    force.do_b()

        elif event == "B":
            print(f"Mediator: {sender} does B")



class BaseForce(ABC):
    def __init__(self, mediator: Station):
        self.mediator = mediator
        self.mediator.forces.append(self)

    def do_a(self):
        self.mediator.notify(self, "A")

    def do_b(self):
        self.mediator.notify(self, "B")


class Plane(BaseForce): ...
class Helicopter(BaseForce): ...


def main(invoker: BaseForce):
    invoker.do_a()


if __name__ == "__main__":
    mediator = Station()
    plane = Plane(mediator)
    helicopter = Helicopter(mediator)

    main(helicopter)

    """
    Mediator: <__main__.Helicopter object at 0x000001E43E006240> does A
    Mediator: <__main__.Plane object at 0x000001E43E0062D0> does B
    """
