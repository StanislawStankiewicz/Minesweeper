MINE_SYMBOL = 'X'


class Board:
    def __init__(self, columns, rows):
        self.board = [[0 for _ in range(columns)] for _ in range(rows)]

    def get_value(self, column, row):
        return self.board[row][column]

    def set_value(self, column, row, value):
        self.board[row][column] = value

    def __str__(self):
        result = ""
        for i, row in enumerate(self.board):
            r = ""
            for value in row:
                r += f"{value} "
            result += f"{r}\n"
        return result


if __name__ == '__main__':
    print(Board(5, 4))
