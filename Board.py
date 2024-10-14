from colorama import Fore, Back

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
                r += self.get_fore_color(value) + self.get_back_color(value) + f" {value} " + Back.RESET + Fore.RESET
            result += f"{r}\n"
        return result

    def get_back_color(self, value):
        if isinstance(value, str):
            return Back.BLACK
        if value == 0:
            return Back.LIGHTBLACK_EX
        if value == 1:
            return Back.BLUE
        if value == 2:
            return Back.CYAN
        if value == 3:
            return Back.GREEN
        if value == 4:
            return Back.LIGHTGREEN_EX
        if value == 5:
            return Back.YELLOW
        if value == 6:
            return Back.LIGHTYELLOW_EX
        if value == 7:
            return Back.LIGHTRED_EX
        if value == 8:
            return Back.RED

        return Back.RESET

    def get_fore_color(self, value):
        if isinstance(value, str):
            return Fore.RESET
        if value == 8:
            return Fore.RESET

        return Fore.BLACK


if __name__ == '__main__':
    print(Board(5, 4))