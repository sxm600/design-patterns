from abc import ABC, abstractmethod


class PathFindingStrategy(ABC):
    @abstractmethod
    def find(self, start: str, end: str): ...


class CarPathFindingStrategy(PathFindingStrategy):
    def find(self, start: str, end: str):
        print(f"Finding car route from {start} to {end}")


class WalkPathFindingStrategy(PathFindingStrategy):
    def find(self, start: str, end: str):
        print(f"Finding walking route from {start} to {end}")


class UserMap:
    def __init__(self, strategy: PathFindingStrategy):
        self.strategy = strategy

    def find(self, start: str, end: str):
        self.strategy.find(start, end)


def main():
    walker = UserMap(WalkPathFindingStrategy())
    driver = UserMap(CarPathFindingStrategy())

    walker.find(start="A", end="B")
    driver.find(start="A", end="B")


if __name__ == "__main__":
    main()

    """
    Finding walking route from A to B
    Finding car route from A to B
    """