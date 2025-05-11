from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Structure:
    name: str

    def collect(self):
        print(f"Collecting from {self.name}")


class GameAI(ABC):
    def __init__(self):
        self.structures = []

    def collect_resources(self):
        for structure in self.structures:
            structure.collect()

    @abstractmethod
    def build_structures(self): ...


    def turn(self):
        self.collect_resources()
        self.build_structures()


class OrcsAI(GameAI):
    def build_structures(self):
        print("Build Orcs structures if no enemies nearby")


def main():
    ai = OrcsAI()
    ai.structures.append(Structure("A"))
    ai.structures.append(Structure("B"))
    ai.turn()


if __name__ == "__main__":
    main()
    
    '''
    Collecting from A
    Collecting from B
    Build Orcs structures if no enemies nearby
    '''