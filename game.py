import pygame
from settings import _Settings
from player import Player
from board import Board


class Game(_Settings):
    def __init__(self, player1_name="Player1", player2_name="Player2"):
        self.player1 = Player(player1_name, self.player1_color, 1)
        self.player2 = Player(player2_name, self.player2_color, 2)
        self.board = Board(self.player1.value, self.player2.value)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Warcaby')
        self.screen.fill(self.background_color)
        self._draw_table()
        self._draw_pieces()

    def _draw_table(self):
        for column in range(0, 8):
            for row in range(0, 8):
                if (row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1):
                    pygame.draw.rect(self.screen, self.color1,
                                     pygame.Rect(row * self.tile_width, column * self.tile_height, self.tile_width,
                                                 self.tile_height))
                    pygame.display.flip()
                else:
                    pygame.draw.rect(self.screen, self.color2,
                                     pygame.Rect(row * self.tile_width, column * self.tile_height, self.tile_width,
                                                 self.tile_height))
                    pygame.display.flip()

    def _draw_pieces(self):
        for column in range(0, 3):
            for row in range(0, 8):
                if (row % 2 != 0 and column % 2 == 0) or (row % 2 == 0 and column % 2 != 0):
                    pygame.draw.circle(self.screen, self.player1_color,
                                       (self.piece_center[0] * (2 * row + 1), self.piece_center[1] * (2 * column + 1)),
                                       self.piece_radius)  # draw player1 pieces
                    pygame.display.flip()
                else:
                    pygame.draw.circle(self.screen, self.player2_color,
                                       (self.piece_center[0] * (2 * row + 1), self.piece_center[1] * (2 * column + 11)),
                                       self.piece_radius)  # draw player2 pieces
                    pygame.display.flip()

    def reset_tile(self, row, column, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(row * self.tile_width, column * self.tile_height,
                                                         self.tile_width, self.tile_height))
        pygame.display.flip()

    def move_piece(self, row, column, curr_row, curr_col):
        self.reset_tile(curr_row, curr_col, self.color1)
        pygame.draw.circle(self.screen, self.player1_color, (self.piece_center[0] * (2 * row + 1),
                           self.piece_center[1] * (2 * column + 1)), self.piece_radius)
        pygame.display.flip()

    def get_tile(self, pos):
        # pos[0] -> x-axis  pos[1] -> y-axis
        row = pos[0] // self.tile_width
        column = pos[1] // self.tile_height
        return row, column

    def color_tile(self, pos, color=(255,22,33)):
        row, column = self.get_tile(pos)
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(row * self.tile_width, column * self.tile_height, self.tile_width,
                                     self.tile_height))
        pygame.display.flip()
