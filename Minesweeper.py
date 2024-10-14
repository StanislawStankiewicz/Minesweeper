import random

from Board import Board, MINE_SYMBOL


class Minesweeper:
    def __init__(self, board_columns, board_rows, mines_amount):
        self.board_columns = board_columns
        self.board_rows = board_rows
        self.mines_amount = mines_amount
        self.mines = set()
        self.board = None

        self.create_board()

    def create_board(self):
        self.validate_args()
        self.board = Board(self.board_columns, self.board_rows)
        self.populate_board()
        self.calculate_fields()

    def validate_args(self):
        total_cells = self.board_rows * self.board_columns
        if self.mines_amount > total_cells:
            raise ValueError(f"Mines amount cannot be larger than total amount of cells!")

    def populate_board(self):
        while len(self.mines) < self.mines_amount:
            self.mines.add(
                (random.randint(0, self.board_columns - 1),
                 random.randint(0, self.board_rows - 1))
            )
        for mine in self.mines:
            self.board.set_value(mine[0], mine[1], MINE_SYMBOL)

    def calculate_fields(self):
        for mine in self.mines:
            self.increment_around(mine)

    def increment_around(self, mine):
        for x in range(mine[0] - 1, mine[0] + 2):
            for y in range(mine[1] - 1, mine[1] + 2):
                if x not in range(0, self.board_columns) or y not in range(0, self.board_rows):
                    continue
                if (x, y) == mine:
                    continue
                value = self.board.get_value(x, y)
                if isinstance(value, str):
                    continue
                self.board.set_value(x, y, value + 1)

if __name__ == '__main__':
    print(Minesweeper(5, 4, 5).board)