import unittest

from Board import Board


class BoardTests(unittest.TestCase):
    def test_creates_board(self):
        num_columns = 3
        num_rows = 4
        board = Board(num_columns, num_rows)

        self.assertEqual(len(board.board), num_rows)
        for column in board.board:
            self.assertEqual(len(column), num_columns)

    def test_get_value(self):
        board = Board(0,0)
        board.board = [[0, 0],
                       [2, 0]]

        self.assertEqual(board.get_value(0, 1), 2)

    def test_set_value(self):
        board = Board(0,0)
        board.board = [[0, 0],
                       [2, 0]]
        board.set_value(1, 0, 2)

        self.assertEqual(board.board[0][1], 2)


if __name__ == '__main__':
    unittest.main()
