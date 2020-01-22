import pygame
import sys
import time
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
                        opponent = game.player2 if game.player1.turn else game.player1
                        #print(piece_pos)
                        if not player.selected_piece:
                            if piece_pos in player:
                                possible_moves = game.find_moves(piece_pos, player.value)
                                player.possible_moves = possible_moves
                                game.display_moves(possible_moves)
                                player.selected_piece = True
                                player.current_position = piece_pos

                        elif player.selected_piece:
                            new_pos = pygame.mouse.get_pos()
                            move = game.get_tile(new_pos)
                            if move in player.possible_moves:
                                game.reset_tile(move, game.color2, player.possible_moves)
                                game.move_piece(move, player.current_position, player.value)
                                if game.is_kill(move, player.current_position):
                                    row, column = (move[0]+player.current_position[0])//2,\
                                                 (move[1]+player.current_position[1])//2
                                    opponent.del_piece((row, column))
                                    game.reset_tile((row, column), game.color2)
                                    player.possible_moves = game.find_kills(move, player.value)
                                    while len(player.possible_moves) > 0:
                                        time.sleep(0.5)
                                        game.move_piece(player.possible_moves[0], move, player.value)
                                        row, column = (move[0] + player.possible_moves[0][0]) // 2, \
                                                      (move[1] + player.possible_moves[0][1]) // 2
                                        opponent.del_piece((row, column))
                                        game.reset_tile((row, column), game.color2)
                                        move = player.possible_moves[0]
                                        player.possible_moves = game.find_kills(move, player.value)
                                    print(player.possible_moves)
                                player.selected_piece = False
                                player.turn = False
                                opponent.turn = True
                            else:
                                # player.selected_piece = False
                                game.reset_tile(move, game.color2, player.possible_moves)
                                if move in player:
                                    player.possible_moves = game.find_moves(move, player.value)
                                    game.display_moves(player.possible_moves)
                                    player.selected_piece = True
                                    player.current_position = move
                                else:
                                    player.selected_piece = False




if __name__ == '__main__':
    main()
