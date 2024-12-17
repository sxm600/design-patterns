from dataclasses import dataclass
from math import sqrt


type number = float | int


@dataclass
class RoundHole:
    radius: number

    def fits(self, round_peg: 'RoundPeg'):
        return self.radius >= round_peg.radius


@dataclass
class RoundPeg:
    radius: number


@dataclass
class SquarePeg:
    width: number


@dataclass
class SquarePegAdapter(RoundPeg):
    square_peg: SquarePeg

    def __init__(self, square_peg: SquarePeg):
        self.radius = square_peg.width * sqrt(2) / 2
        self.square_peg = square_peg


def main(round_hole: RoundHole, round_peg: RoundPeg) -> None:
    print(round_peg, round_hole.fits(round_peg))

if __name__ == '__main__':
    round_hole = RoundHole(5)
    round_peg = RoundPeg(5)
    square_peg = SquarePeg(5)

    main(round_hole, round_peg)  # RoundPeg(radius=5) True
    main(round_hole, SquarePegAdapter(square_peg))  # SquarePegAdapter(radius=3.5355339059327378, square_peg=SquarePeg(width=5)) True
