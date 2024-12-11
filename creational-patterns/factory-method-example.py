from abc import abstractmethod, ABC
from typing import override
import platform


class Dialog:
    @abstractmethod
    def create_button(self) -> 'Button': ...

    def render(self):
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
    def render(self): ...

    @abstractmethod
    def on_click(self, f: callable): ...


class WindowsButton(Button):
    @override
    def render(self):
        print('Windows button rendered.')

    @override
    def on_click(self, f: callable):
        f()
        print('Windows button was clicked.')


class WebButton(Button):
    @override
    def render(self):
        print('Web button rendered.')

    @override
    def on_click(self, f: callable):
        f()
        print('Web button was clicked.')


def main(system: str) -> None:
    if system == 'Windows':
        dialog = WindowsDialog()
    elif system == 'Web':
        dialog = WebDialog()
    else:
        raise Exception(f'Unsupported platform system passed ({system}).')

    dialog.render()

    '''
    Output:
    
    Click!
    Windows button was clicked.
    Windows button rendered.
    '''


if __name__ == '__main__':
    main(platform.system())  # in my case 'Windows'
