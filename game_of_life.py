from abc import abstractmethod, ABC
from time import sleep


class AbstractLifeGameBoard(ABC):
    def __init__(self, width: int = 3, height: int = 3):
        """Return a string representation of a board.

        Use small o for alive cells and period for empty cells.
        E.g. for board 3x3 with simplest oscillator:
        .o.
        .o.
        .o.
        """
        pass

    def __str__(self):
        """Make a cell alive."""
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
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[False] * self.width for _ in range(self.height)]

    def place_cell(self, row: int, col: int):
        if 0 <= row < self.height and 0 <= col < self.width:
            self.board[row][col] = True
        else:
            raise ValueError

    def toggle_cell(self, row: int, col: int) -> None:
        if 0 <= row < self.height and 0 <= col < self.width:
            if self.board[row][col] == [True]:
                self.board[row][col] = False
            elif self.board[row][col] == [False]:
                self.board[row][col] = False
        else:
            raise ValueError

    def live_neighbors(self, row: int, col: int) -> int:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                count += self.is_alive(row + i, col + j)
        return count

    def next(self) -> None:
        next_board = [[False] * self.width for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                live_neighbors = self.live_neighbors(i, j)
                if self.board[i][j]:
                    if live_neighbors == 2 or live_neighbors == 3:
                        next_board[i][j] = True
                elif live_neighbors == 3:
                    next_board[i][j] = True
        self.board = next_board

    def is_alive(self, row: int, col: int) -> bool:
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.board[row][col]
        else:
            return False

    def __str__(self):
        output = ""
        for row in self.board:
            for cell in row:
                output += "o " if cell else "- "
            output += "\n"
        return output


c = CELL_SYMBOL = "o"

if __name__ == "__main__":
    board = Board(10, 10)
    for i in range(5):
        board.place_cell(3, i)

    for i in range(10):
        print(board)
        board.next()
        sleep(1)
