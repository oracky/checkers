import unittest
from game import Game


class GameTest(unittest.TestCase):
    def test_move_piece(self):
        game = Game()
        before_pos = (0, 7)
        after_pos = (0, 6)

        game.move_piece(after_pos, before_pos, 1)
        self.assertIn(after_pos, game.player1)

    def test_get_tile(self):
        pos = (15, 15)
        game = Game()
        tile = game.get_tile(pos)
        self.assertEqual(tile, (0, 0))

    @staticmethod
    def test_is_kill():
        after_pos = (0, 7)
        before_pos = (2, 5)
        game = Game()
        assert game.is_kill(after_pos, before_pos)

    @staticmethod
    def test_is_queen():
        pos = (5, 0)
        game = Game()
        assert game.is_queen(pos, 1)

    @staticmethod
    def test_find_moves():
        pos = (0, 0)
        game = Game()
        moves = game.find_moves(pos)
        assert not moves


if __name__ == '__main__':
    unittest.main()
