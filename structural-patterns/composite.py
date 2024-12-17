from abc import ABC, abstractmethod
from dataclasses import dataclass, field


type number = float | int


class Graphic(ABC):
    @abstractmethod
    def move(self, x, y) -> None: ...

    @abstractmethod
    def draw(self) -> None: ...


@dataclass
class Dot(Graphic):
    x: number
    y: number

    def move(self, x, y) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f'Drawing dot at: {self.x, self.y}')


@dataclass
class Circle(Graphic):
    center: Dot
    radius: number

    def move(self, x, y) -> None:
        self.center.move(x, y)

    def draw(self) -> None:
        print(f'Drawing circle at: {self.center} with radius {self.radius}')


@dataclass
class CompoundGraphic(Graphic):
    children: list[Graphic] = field(default_factory=list)

    def add(self, graphic: Graphic):
        self.children.append(graphic)

    def remove(self, graphic: Graphic):
        self.children.remove(graphic)

    def move(self, x, y) -> None:
        for child in self.children:
            child.move(x, y)

    def draw(self) -> None:
        for child in self.children:
            child.draw()


def main(group: CompoundGraphic) -> None:
    print('Drawing initial group:')
    group.draw()

    group.move(5, 5)
    print('Drawing group after moving by (5, 5):')
    group.draw()

if __name__ == '__main__':
    group = CompoundGraphic()
    group.add(Dot(2, 2))
    group.add(Dot(3, 3))
    group.add(Circle(Dot(2, 2), 2))

    main(group)
    '''
    Output:
    
    Drawing initial group:
    Drawing dot at: (2, 2)
    Drawing dot at: (3, 3)
    Drawing circle at: Dot(x=2, y=2) with radius 2
    
    Drawing group after moving by (5, 5):
    Drawing dot at: (7, 7)
    Drawing dot at: (8, 8)
    Drawing circle at: Dot(x=7, y=7) with radius 2
    '''