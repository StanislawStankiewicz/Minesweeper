from colorama import Fore, Back

MINE_SYMBOL = 'X'

background_color_schema = {
    MINE_SYMBOL: Back.BLACK,
    0: Back.LIGHTBLACK_EX,
    1: Back.BLUE,
    2: Back.CYAN,
    3: Back.GREEN,
    4: Back.LIGHTGREEN_EX,
    5: Back.YELLOW,
    6: Back.LIGHTYELLOW_EX,
    7: Back.LIGHTRED_EX,
    8: Back.RED
}

foreground_color_schema = {
    MINE_SYMBOL: Fore.RESET,
    8: Fore.RESET
}

def get_fore_color(value):
    return foreground_color_schema.get(value, Fore.BLACK)

def get_back_color(value):
    return background_color_schema.get(value)


class Board:
    def __init__(self, columns, rows):
        self.board = [[0 for _ in range(columns)] for _ in range(rows)]

    def get_value(self, column, row):
        return self.board[row][column]

    def set_value(self, column, row, value):
        self.board[row][column] = value

    def __str__(self):
        result = "    "
        for i in range(len(self.board[0])):
            result += f"{i}. "
        result += "\n"
        for i, row in enumerate(self.board):
            r = f"{i}. "
            for value in row:
                r += get_fore_color(value) + get_back_color(value) + f" {value} " + Back.RESET + Fore.RESET
            result += f"{r}\n"
        return result


if __name__ == '__main__':
    print(Board(5, 4))