class Board:
    def __init__(self, pl1_value, pl2_value):
        self.player1 = pl1_value
        self.player2 = pl2_value
        self.player1_queen = -self.player1
        self.player2_queen = -self.player2
        self.empty = 0
        self.board = [
            [self.empty, self.player2, self.empty, self.player2, self.empty, self.player2, self.empty, self.player2],
            [self.player2, self.empty, self.player2, self.empty, self.player2, self.empty, self.player2, self.empty],
            [self.empty, self.player2, self.empty, self.player2, self.empty, self.player2, self.empty, self.player2],
            [self.empty for i in range(0, 8)],
            [self.empty for i in range(0, 8)],
            [self.player1, self.empty, self.player1, self.empty, self.player1, self.empty, self.player1, self.empty],
            [self.empty, self.player1, self.empty, self.player1, self.empty, self.player1, self.empty, self.player1],
            [self.player1, self.empty, self.player1, self.empty, self.player1, self.empty, self.player1, self.empty]
        ]

    def update_board(self):
        pass