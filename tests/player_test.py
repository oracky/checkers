import unittest
from player import Player


class PlayerTest(unittest.TestCase):
    def test_set_name(self):
        name = "michal"
        player = Player("Unknown", 1, 1)
        player.set_player_name(name)
        self.assertEqual(player.name, name)

    def test_del_piece(self):
        player = Player("Unknown", 1, 1)
        pos = (0, 7)
        player.del_piece(pos)
        self.assertNotIn(pos, player.pieces_list)

if __name__ == '__main__':
    unittest.main()
