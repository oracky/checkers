from piece import Piece


class Player:
    def __init__(self, name, color, value=1,):
        self.name = name
        self.color = color
        self.value = value
        self.turn = False
        self.selected_piece = False
        self.current_position = (0, 0)
        self.possible_moves = []
        self.winner = False
        self.no_more_moves = True
        if self.value != 1:
            self.pieces_list = [
                Piece((1, 0)), Piece((3, 0)), Piece((5, 0)), Piece((7, 0)),
                Piece((0, 1)), Piece((2, 1)), Piece((4, 1)), Piece((6, 1)),
                Piece((1, 2)), Piece((3, 2)), Piece((5, 2)), Piece((7, 2))
            ]
        else:
            self.pieces_list = [
                Piece((0, 7)), Piece((2, 7)), Piece((4, 7)), Piece((6, 7)),
                Piece((1, 6)), Piece((3, 6)), Piece((5, 6)), Piece((7, 6)),
                Piece((0, 5)), Piece((2, 5)), Piece((4, 5)), Piece((6, 5))
            ]

    def __str__(self):
        return self.name

    def __contains__(self, pos):
        for piece in self.pieces_list:
            if piece.position == pos:
                return True
        return False

    def set_player_name(self, name):
        self.name = name

    def del_piece(self, pos):
        for i, piece in enumerate(self.pieces_list):
            if piece.position == pos:
                del self.pieces_list[i]
                break
