import unittest

from Minesweeper import Minesweeper


class MyTestCase(unittest.TestCase):
    def test_throws_when_too_many_mines(self):
        self.assertRaises(ValueError, lambda: Minesweeper(1, 1, 2))

    def test_creates_board(self):
        num_columns = 3
        num_rows = 4
        mines_amount = 8
        game = Minesweeper(num_columns, num_rows, mines_amount)

        self.assertEqual(len(game.board.board), num_rows)
        for row in game.board.board:
            self.assertEqual(len(row), num_columns)

    def test_populates_mines(self):
        num_columns = 3
        num_rows = 4
        mines_amount = 8
        game = Minesweeper(num_columns, num_rows, mines_amount)

        self.assertEqual(len(game.mines), mines_amount)
        # assert not throws
        for mine in game.mines:
            game.board.get_value(mine[0], mine[1])


if __name__ == '__main__':
    unittest.main()
