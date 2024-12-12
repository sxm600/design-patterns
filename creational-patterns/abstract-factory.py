from abc import ABC, abstractmethod
from typing import override


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> 'Button': ...

    @abstractmethod
    def create_checkbox(self) -> 'CheckBox': ...


class WinFactory(GUIFactory):
    @override
    def create_button(self) -> 'Button':
        return WinButton()

    @override
    def create_checkbox(self) -> 'CheckBox':
        return WinCheckBox()


class MacFactory(GUIFactory):
    @override
    def create_button(self) -> 'Button':
        return MacButton()

    @override
    def create_checkbox(self) -> 'CheckBox':
        return MacCheckBox()


class Button(ABC):
    @abstractmethod
    def paint(self) -> None: ...


class WinButton(Button):
    @override
    def paint(self) -> None:
        print('Rendering Windows button.')


class MacButton(Button):
    @override
    def paint(self) -> None:
        print('Rendering Mac button.')


class CheckBox(ABC):
    @abstractmethod
    def paint(self) -> None: ...


class WinCheckBox(CheckBox):
    @override
    def paint(self) -> None:
        print('Rendering Windows checkbox.')


class MacCheckBox(CheckBox):
    @override
    def paint(self) -> None:
        print('Rendering Mac checkbox.')


def main(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.paint()
    checkbox.paint()


if __name__ == '__main__':
    main(WinFactory())
    '''
    Output:
    
    Rendering Windows button.
    Rendering Windows checkbox.
    '''


    main(MacFactory())
    '''
    Rendering Mac button.
    Rendering Mac checkbox.
    '''
