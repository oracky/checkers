import pygame
from settings import Settings
from player import Player
from board import Board


class Game(Settings):
    def __init__(self, player1_name="Player1", player2_name="Player2"):
        self.player1 = Player(player1_name, self.player1_color, 1)
        self.player2 = Player(player2_name, self.player2_color, 2)
        self.game_over = False
        self.turn = True
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        self.winner_font = pygame.font.SysFont('Arial', 45)
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
                    pygame.draw.circle(self.screen, self.player2_color,
                                       (self.piece_center[0] * (2 * row + 1), self.piece_center[1] * (2 * column + 1)),
                                       self.piece_radius)  # draw player2 pieces
                    pygame.display.flip()
                else:
                    pygame.draw.circle(self.screen, self.player1_color,
                                       (self.piece_center[0] * (2 * row + 1), self.piece_center[1] * (2 * column + 11)),
                                       self.piece_radius)  # draw player1 pieces
                    pygame.display.flip()

    def reset_tile(self, position, color, *args):
        if len(args) > 0:
            for arg in args:
                for pos in arg:
                    pygame.draw.rect(self.screen, color,
                                     pygame.Rect(pos[0] * self.tile_width, pos[1] * self.tile_height,
                                                 self.tile_width, self.tile_height))
                    pygame.display.flip()
        else:
            pygame.draw.rect(self.screen, color, pygame.Rect(position[0] * self.tile_width, position[1] * self.tile_height,
                                                             self.tile_width, self.tile_height))
            pygame.display.flip()

    def move_piece(self, new_position, current_position, player=1):
        self.reset_tile(current_position, self.color2)
        color = self.player1_color if player == 1 else self.player2_color
        turn = self.player1 if player == 1 else self.player2
        pygame.draw.circle(self.screen, color, (self.piece_center[0] * (2 * new_position[0] + 1),
                           self.piece_center[1] * (2 * new_position[1] + 1)), self.piece_radius)
        pygame.display.flip()
        self.update_piece(new_position, current_position, turn.value)

    def update_piece(self, new_position, current_position, player=1):
        turn = self.player1 if player == 1 else self.player2
        for piece in turn.pieces_list:
            if piece.position == current_position:
                piece.position = new_position

    def get_tile(self, pos):
        # pos[0] -> x-axis  pos[1] -> y-axis
        row = pos[0] // self.tile_width
        column = pos[1] // self.tile_height
        return row, column

    def color_tile(self, pos, color=(255, 22, 33)):
        row, column = pos[0], pos[1]
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(row * self.tile_width, column * self.tile_height, self.tile_width,
                                     self.tile_height))
        pygame.display.flip()

    def find_moves(self, pos, player=1):
        moves = []
        north_east = (pos[0]+1, pos[1]-1)
        north_west = (pos[0]-1, pos[1]-1)
        south_east = (pos[0]+1, pos[1]+1)
        south_west = (pos[0]-1, pos[1]+1)

        if player == 1:
            if (north_east not in self.player1 and north_east not in self.player2) and north_east[0] < 8 and north_east[1] >= 0:
                moves.append(north_east)
            if (north_west not in self.player1 and north_west not in self.player2) and north_west[0] >= 0 and north_west[1] >= 0:
                moves.append(north_west)
        else:
            if (south_east not in self.player2 and south_east not in self.player1) and south_east[0] < 8 and south_east[1] < 8:
                moves.append(south_east)
            if (south_west not in self.player2 and south_west not in self.player1) and south_west[0] >= 0 and south_west[1] < 8:
                moves.append(south_west)
        moves += self.find_kills(pos, player)
        return moves

    def find_kills(self, pos, value=1):
        kills = []
        north_east_short = (pos[0] + 1, pos[1] - 1)
        north_west_short = (pos[0] - 1, pos[1] - 1)
        south_east_short = (pos[0] + 1, pos[1] + 1)
        south_west_short = (pos[0] - 1, pos[1] + 1)
        north_east = (pos[0] + 2, pos[1] - 2)
        north_west = (pos[0] - 2, pos[1] - 2)
        south_east = (pos[0] + 2, pos[1] + 2)
        south_west = (pos[0] - 2, pos[1] + 2)

        player = self.player1 if value == 1 else self.player2
        opponent = self.player2 if value == 1 else self.player1

        if (north_east_short in opponent and north_east not in player and north_east not in opponent)\
                and north_east[0] < 8 and north_east[1] >= 0:
            kills.append(north_east)
        if (north_west_short in opponent and north_west not in player and north_west not in opponent)\
                and north_west[0] >= 0 and north_west[1] >= 0:
            kills.append(north_west)
        if (south_east_short in opponent and south_east not in player and south_east not in opponent)\
                and south_east[0] < 8 and south_east[1] < 8:
            kills.append(south_east)
        if (south_west_short in opponent and south_west not in player and south_west not in opponent)\
                and south_west[0] >= 0 and south_west[1] < 8:
            kills.append(south_west)
        return kills

    def is_kill(self, after_pos, before_pos):
        if abs(after_pos[0] - before_pos[0]) == 2:
            return True
        return False

    def display_moves(self, moves):
        for move in moves:
            self.color_tile(move, self.move_color)

    def draw_turn_rect(self, value=1):
        player = self.player1 if value == 1 else self.player2
        pygame.draw.rect(self.screen, player.color,
                         pygame.Rect(8.5 * self.tile_width, 4 * self.tile_height, self.tile_width * 2,
                                     self.tile_height))
        pygame.display.flip()
        self.screen.blit(self.font.render(player.name, True, self.color1),
                         (8.6 * self.tile_width + 10, 4.3 * self.tile_height))
        pygame.display.update()

    def draw_winner_rect(self, value=1):
        player = self.player1 if value == 1 else self.player2
        pygame.draw.rect(self.screen, player.color,
                         pygame.Rect(0, 2 * self.tile_height, self.screen_width,
                                     4 * self.tile_height))
        pygame.display.flip()
        self.screen.blit(self.winner_font.render(f"{player.name} WINS!!!", True, self.color1),
                         (self.screen_width // 4, self.screen_height // 2))
        pygame.display.update()