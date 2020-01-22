import pygame
import sys
from game import Game
from piece import Piece


def main():
    game = Game()
    game.player1.turn = True
    turn = True
    while not game.game_over:
        while turn:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        piece_pos = game.get_tile(pos)
                        player = game.player1 if game.player1.turn else game.player2
                        next_player = game.player2 if game.player1.turn else game.player1
                        #print(piece_pos)
                        if not player.selected_piece:
                            if piece_pos in player:
                                possible_moves = game.find_moves(piece_pos, player.value)
                                player.possible_moves = possible_moves
                                print(possible_moves)
                                game.display_moves(possible_moves)
                                player.selected_piece = True
                                player.current_position = piece_pos

                        elif player.selected_piece:
                            new_pos = pygame.mouse.get_pos()
                            move = game.get_tile(new_pos)
                            if move in player.possible_moves:
                                game.reset_tile(move, game.color2, player.possible_moves)
                                game.move_piece(move, player.current_position, player.value)
                                player.selected_piece = False
                                player.turn = False
                                next_player.turn = True
                            else:
                                player.selected_piece = False
                                game.reset_tile(move, game.color2, player.possible_moves)





if __name__ == '__main__':
    main()
