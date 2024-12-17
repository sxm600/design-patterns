from abc import ABC, abstractmethod
from typing import override, Any
from dataclasses import dataclass


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data: Any) -> None: ...

    @abstractmethod
    def read_data(self) -> Any: ...


@dataclass
class FileDataSource(DataSource):
    filename: str

    @override
    def write_data(self, data: Any) -> None:
        print(f'Writing data to: {self.filename}')

    @override
    def read_data(self) -> Any:
        print(f'Reading data from: {self.filename}')


@dataclass
class EncryptionDecorator(DataSource):
    data_source: DataSource

    def write_data(self, data: Any) -> None:
        print('Encrypting data...')
        self.data_source.write_data(data)

    def read_data(self) -> Any:
        self.data_source.read_data()
        print('Decrypting data...')


def main(data_source: DataSource) -> None:
    data_source.write_data('Hello World!')
    data_source.read_data()

if __name__ == '__main__':
    source = FileDataSource('data.txt')

    main(source)
    '''
    Output:
    
    Writing data to: data.txt
    Reading data from: data.txt
    '''

    main(EncryptionDecorator(source))
    '''
    Output:
    
    Encrypting data...
    Writing data to: data.txt
    Reading data from: data.txt
    Decrypting data...
    '''
