import unittest
from typing import Tuple

from piece import Piece


class PieceTest(unittest.TestCase):
    def test_change_position(self):
        piece = Piece((0, 7))
        pos = (1, 6)
        piece.change_position(pos)
        self.assertEqual(pos, piece.position)

if __name__ == '__main__':
    unittest.main()
