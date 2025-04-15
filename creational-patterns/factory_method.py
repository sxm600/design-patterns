from abc import ABC, abstractmethod
from typing import override


class Dialog:
    @abstractmethod
    def create_button(self) -> 'Button': ...

    def render(self) -> None:
        button = self.create_button()
        button.on_click(lambda: print('Click!'))
        button.render()


class WindowsDialog(Dialog):
    @override
    def create_button(self) -> 'Button':
        return WindowsButton()


class WebDialog(Dialog):
    @override
    def create_button(self) -> 'Button':
        return WebButton()


class Button(ABC):
    @abstractmethod
    def render(self) -> None: ...

    @abstractmethod
    def on_click(self, f: callable) -> None: ...


class WindowsButton(Button):
    @override
    def render(self) -> None:
        print('Windows button rendered.')

    @override
    def on_click(self, f: callable) -> None:
        print(f'Binding \'on_click\' function to Windows button.')


class WebButton(Button):
    @override
    def render(self) -> None:
        print('Web button rendered.')

    @override
    def on_click(self, f: callable) -> None:
        print(f'Binding \'on_click\' function to Web button.')


def main(dialog: Dialog) -> None:
    dialog.render()


if __name__ == '__main__':
    main(WindowsDialog())
    '''
    Output:

    Binding 'on_click' function to Windows button.
    Windows button rendered.
    '''

    main(WebDialog())
    '''
    Output:
    
    Binding 'on_click' function to Web button.
    Web button rendered.
    '''
