from threading import Lock, Thread


class Singleton(type):
    _instances = dict()
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self, conn_string: str):
        self.conn_string = conn_string

    def connect(self): ...


def main(db: Database) -> None:
    print(db.conn_string, id(db))


if __name__ == '__main__':
    process1 = Thread(target=main, args=(Database('conn1'),))
    process2 = Thread(target=main, args=(Database('conn2'),))

    process1.start()  # conn1 1726188478080
    process2.start()  # conn1 1726188478080
