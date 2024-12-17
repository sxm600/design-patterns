from abc import ABC, abstractmethod
from typing import override


class RemoteControl:
    def __init__(self, device: 'Device'):
        self.device = device

    def volume_up(self, value: int):
        self.device.volume_up(value)

    def volume_down(self, value: int):
        self.device.volume_down(value)


class Device(ABC):
    @abstractmethod
    def volume_up(self, value: int) -> None: ...

    @abstractmethod
    def volume_down(self, value: int) -> None: ...


class TV(Device):
    @override
    def volume_up(self, value: int) -> None:
        print(f'TV volume is up by {value}')

    @override
    def volume_down(self, value: int) -> None:
        print(f'TV volume is down by {value}')


class Radio(Device):
    @override
    def volume_up(self, value: int) -> None:
        print(f'Radio volume is up by {value}')

    @override
    def volume_down(self, value: int) -> None:
        print(f'Radio volume is down by {value}')


def main(remote_control: RemoteControl) -> None:
    remote_control.volume_up(10)
    remote_control.volume_down(10)

if __name__ == '__main__':
    main(RemoteControl(TV()))
    '''
    Output:
    
    TV volume is up by 10
    TV volume is down by 10
    '''

    main(RemoteControl(Radio()))
    '''
    Radio volume is up by 10
    Radio volume is down by 10
    '''
