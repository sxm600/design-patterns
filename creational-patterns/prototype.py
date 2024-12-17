from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


type number = float | int


class Shape(ABC):
    @abstractmethod
    def area(self) -> number: ...

    @abstractmethod
    def clone(self) -> 'Shape': ...


@dataclass
class Rectangle(Shape):
    length: float | int
    width: int

    def area(self) -> number:
        return self.length * self.width

    def clone(self) -> 'Rectangle':
        return Rectangle(self.length, self.width)


@dataclass
class Circle(Shape):
    radius: number

    def area(self) -> number:
        return math.pi * (self.radius ** 2)

    def clone(self) -> 'Circle':
        return Circle(self.radius)


def main(shape: Shape) -> None:
    print(f'Shape: {shape} addr({id(shape)})')
    print(f'Area: {shape.area()}')
    print(f'Clone: {(clone := shape.clone())} addr({id(clone)})')

if __name__ == '__main__':
    main(Rectangle(5, 10))
    '''
    Output:
    
    Shape: Rectangle(length=5, width=10) addr(2369989567136)
    Area: 50
    Clone: Rectangle(length=5, width=10) addr(2369957669168)
    '''

    main(Circle(2))
    '''
    Output:
    
    Shape: Circle(radius=2) addr(2369957669168)
    Area: 12.566370614359172
    Clone: Circle(radius=2) addr(2369985112368)
    '''
