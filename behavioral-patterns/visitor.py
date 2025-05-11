from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor'): ...


class Dot(Shape):
    def accept(self, visitor: 'Visitor'):
        visitor.visit_dot(self)


class Circle(Shape):
    def accept(self, visitor: 'Visitor'):
        visitor.visit_circle(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot: Dot): ...

    @abstractmethod
    def visit_circle(self, circle: Circle): ...


class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot):
        print('XML: Visiting dot...')

    def visit_circle(self, circle: Circle):
        print('XML: Visiting circle...')


def main():
    visitor = XMLExportVisitor()
    visitor.visit_dot(Dot())
    visitor.visit_circle(Circle())


if __name__ == '__main__':
    main()
    
    '''
    XML: Visiting dot...
    XML: Visiting circle...
    '''