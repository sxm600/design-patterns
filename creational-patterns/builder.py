from dataclasses import dataclass


@dataclass
class Pizza:
    size: int
    sauces: list[str]
    toppings: list[str]

    def __init__(self, builder: 'Pizza.Builder'):
        self.size = builder.size
        self.sauces = builder.sauces
        self.toppings = builder.toppings


    class Builder:
        def __init__(self, size: int):
            self.size: int = size
            self.sauces: list[str] = []
            self.toppings: list[str] = []

        def ketchup(self) -> 'Pizza.Builder':
            self.sauces.append('ketchup')
            return self

        def mayo(self) -> 'Pizza.Builder':
            self.sauces.append('mayo')
            return self

        def cheddar(self) -> 'Pizza.Builder':
            self.toppings.append('cheddar')
            return self

        def mozzarella(self) -> 'Pizza.Builder':
            self.toppings.append('mozzarella')
            return self

        def pepperoni(self) -> 'Pizza.Builder':
            self.toppings.append('pepperoni')
            return self

        def build(self) -> 'Pizza':
            return Pizza(self)


def main() -> None:
    print(
        Pizza.Builder(24)
            .ketchup()
            .mozzarella()
            .pepperoni()
            .build()
    )

    #  Pizza(size=24, sauces=['ketchup'], toppings=['mozzarella', 'pepperoni'])

if __name__ == '__main__':
    main()
