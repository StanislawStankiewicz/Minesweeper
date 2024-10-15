from colorama import Fore, Back
from Board import MINE_SYMBOL
from Minesweeper import Minesweeper

background_color_schema = {
    MINE_SYMBOL: Back.BLACK,
    0: Back.LIGHTBLACK_EX,
    " ": Back.LIGHTBLACK_EX,
    1: Back.BLUE,
    2: Back.CYAN,
    3: Back.GREEN,
    4: Back.LIGHTGREEN_EX,
    5: Back.YELLOW,
    6: Back.LIGHTYELLOW_EX,
    7: Back.RED,
    8: Back.LIGHTRED_EX
}

foreground_color_schema = {
    MINE_SYMBOL: Fore.RESET,
}

def _get_fore_color(value):
    return foreground_color_schema.get(value, Fore.BLACK)

def _get_back_color(value):
    return background_color_schema.get(value)

def _get_column_width(columns):
    pass


# def pretty(board):
#     result = "    "
#     for i in range(len(board[0])):
#         result += f"{i}. "
#     result += "\n"
#     for i, row in enumerate(board):
#         r = f"{i}. "
#         for value in row:
#             if value == 0:
#                 value = " "
#             r += _get_fore_color(value) + _get_back_color(value) + f" {value} " + Back.RESET + Fore.RESET
#         result += f"{r}\n"
#     return result


class Cell:
    def __init__(self, value, padding):
        self.rows = []
        self.value = value
        self.create_cell_rows(value, padding)

    def create_cell_rows(self, value, padding):
        side = 2 * padding + 3
        horizontal_unit = " "
        self.rows.append(horizontal_unit * padding + f" {value} " + horizontal_unit * padding)
        if padding == 2:
            filling = horizontal_unit * side
            self.rows.insert(0, filling)
            self.rows.append(filling)

    def __str__(self):
        result = ""
        for row in self.rows:
            result += f"{row}\n"
        return result


class BoardPrinter:
    def __init__(self, board):
        self.board = board
        self.cells = []
        padding = self._calculate_padding(len(board[0]), len(board))
        for row in board:
            self.cells.append([Cell(value, padding) for value in row])

    def _calculate_padding(self, columns, rows):
        max_len = len(str(max(columns, rows)))
        if max_len >= 2:
            return 2
        if max_len == 1:
            return 1
        return 0

    def print(self):
        result = []
        for row in self.cells:
            for result_row in self._connect_cells(row):
                result.append(result_row)
        for row in result:
            print(row)

    def _connect_cells(self, cells):
        result_rows = [""] * len(cells[0].rows)
        for cell in cells:
            for i, cell_row in enumerate(cell.rows):
                result_rows[i] += _get_back_color(cell.value) + _get_fore_color(cell.value) + cell_row + Fore.RESET + Back.RESET
        return result_rows




if __name__ == '__main__':
    side = 100
    mines_amount = int(side * side * 0.15)
    BoardPrinter(Minesweeper(side, side, mines_amount).board.board).print()
    # print(Cell(3, 1))
    # print(_connect_cells([Cell(3, 0), Cell(2, 0)]))