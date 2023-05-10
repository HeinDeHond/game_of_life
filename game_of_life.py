from abc import abstractmethod, ABC
from time import sleep


class AbstractLifeGameBoard(ABC):
    def __init__(self, width: int = 3, height: int = 3):
        pass

    def __str__(self):
        """Return a string representation of a board.

        Use small o for alive cells and period for empty cells.
        E.g. for board 3x3 with simplest oscillator:
        .o.
        .o.
        .o.
        """
        pass

    @abstractmethod
    def place_cell(self, row: int, col: int):
        """Make a cell alive."""
        pass

    @abstractmethod
    def toggle_cell(self, row: int, col: int) -> None:
        """Invert state of the cell."""
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def is_alive(self, row: int, col: int) -> bool:
        pass


class Board(AbstractLifeGameBoard):
    """Put your solution here"""

    pass


c = CELL_SYMBOL = "o"


if __name__ == "__main__":
    board = Board(3, 3)
    for i in range(3):
        board.place_cell(1, i)

    for i in range(100):
        print(board)
        board.next()
        sleep(0.5)
