class Piece:
    def __init__(self, position, queen=False):
        self.position = position
        self.queen = queen

    def change_position(self, new_pos):
        self.position = new_pos
