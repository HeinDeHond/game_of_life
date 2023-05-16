import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
)
from game_of_life import Board


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.board = Board(10, 10)

        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()

        self.generation_label = QLabel("Generation: 0")
        vbox.addWidget(self.generation_label)

        self.grid_layout = QGridLayout()
        self.create_grid()
        vbox.addLayout(self.grid_layout)

        next_button = QPushButton("Next")
        next_button.clicked.connect(self.next_generation)
        vbox.addWidget(next_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_board)
        vbox.addWidget(clear_button)

        self.setLayout(vbox)

        self.setWindowTitle("Game of Life")
        self.show()

    def create_grid(self):
        for row in range(self.board.height):
            for col in range(self.board.width):
                cell = Cell(self.board, row, col)
                self.grid_layout.addWidget(cell, row, col)

    def next_generation(self):
        self.board.next()
        self.generation_label.setText(f"Generation: {self.board.generation}")
        for row in range(self.board.height):
            for col in range(self.board.width):
                cell = self.grid_layout.itemAtPosition(row, col).widget()
                cell.update_state()

    def clear_board(self):
        self.board.clear()
        self.generation_label.setText("Generation: 0")
        for row in range(self.board.height):
            for col in range(self.board.width):
                cell = self.grid_layout.itemAtPosition(row, col).widget()
                cell.update_state()


class Cell(QLabel):
    def __init__(self, board, row, col):
        super().__init__()

        self.board = board
        self.row = row
        self.col = col

        self.setFixedSize(20, 20)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 1px solid black;")

        self.update_state()

    def update_state(self):
        if self.board.board[self.row][self.col]:
            self.setStyleSheet("background-color: black;")
        else:
            self.setStyleSheet("background-color: white;")

    def mousePressEvent(self, event):
        self.board.toggle_cell(self.row, self.col)
        self.update_state()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_window = GameWindow()
    sys.exit(app.exec())
