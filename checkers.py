import pygame
import sys
import time
from game import Game
from piece import Piece


def main():

    # Initialize game
    game = Game()

    # Get players name from command line
    if len(sys.argv) >= 2:
        game.player1.set_player_name(sys.argv[1])
        game.player2.set_player_name(sys.argv[2])

    # Setting turn
    game.player1.turn = True
    game.draw_turn_rect(game.player1.value)

    while not game.game_over:
        while game.turn:
            while True:
                player = game.player1 if game.player1.turn else game.player2
                opponent = game.player2 if game.player1.turn else game.player1

                # Assuming player has no more available moves (if no then he loses)
                player.no_more_moves = True

                # Checking if someone has already won
                if len(player.pieces_list) == 0:
                    opponent.winner = True
                    game.game_over = True
                    game.turn = False
                    break

                # Checking if there are still possible moves
                for piece in player.pieces_list:
                    temp_pos = piece.position
                    temp_possible_moves = game.find_moves(temp_pos, player.value)
                    if len(temp_possible_moves) != 0:
                        player.no_more_moves = False
                        break
                if player.no_more_moves:
                    opponent.winner = True
                    game.game_over = True
                    game.turn = False
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    if event.type == pygame.MOUSEBUTTONUP:

                        # Getting position on a board
                        pos = pygame.mouse.get_pos()
                        piece_pos = game.get_tile(pos)

                        # Checking if there are still possible moves
                        for piece in player.pieces_list:
                            temp_pos = piece.position
                            temp_possible_moves = game.find_moves(temp_pos, player.value)
                            if len(temp_possible_moves) != 0:
                                player.no_more_moves = False
                                break
                        if player.no_more_moves:
                            opponent.winner = True
                            game.game_over = True
                            game.turn = False
                            break
                        else:
                            # Selecting piece to move
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

                                    # Check if piece became queen
                                    if game.is_queen(move, player.value):
                                        game.promote_to_queen(move, player.value, True)

                                    # Looking for kill to make
                                    if game.is_kill(move, player.current_position, player.value):
                                        row, column = (move[0]+player.current_position[0])//2,\
                                                     (move[1]+player.current_position[1])//2
                                        opponent.del_piece((row, column))
                                        game.reset_tile((row, column), game.color2)
                                        player.possible_moves = game.find_kills(move, player.value)

                                        # Looking for next possible kills
                                        while len(player.possible_moves) > 0:
                                            time.sleep(0.5)
                                            game.move_piece(player.possible_moves[0], move, player.value)

                                            # Check if piece became queen
                                            if game.is_queen(player.possible_moves[0], player.value):
                                                game.promote_to_queen(player.possible_moves[0], player.value, True)

                                            row, column = (move[0] + player.possible_moves[0][0]) // 2, \
                                                          (move[1] + player.possible_moves[0][1]) // 2
                                            opponent.del_piece((row, column))
                                            game.reset_tile((row, column), game.color2)
                                            move = player.possible_moves[0]
                                            player.possible_moves = game.find_kills(move, player.value)
                                    player.selected_piece = False
                                    player.turn = False
                                    opponent.turn = True
                                    game.draw_turn_rect(opponent.value)

                                else:
                                    game.reset_tile(move, game.color2, player.possible_moves)
                                    if move in player:
                                        player.possible_moves = game.find_moves(move, player.value)
                                        game.display_moves(player.possible_moves)
                                        player.selected_piece = True
                                        player.current_position = move
                                    else:
                                        player.selected_piece = False

    # Displaying winner
    winner = game.player1 if game.player1.winner else game.player2
    game.draw_winner_rect(winner.value)

    # Waiting for new game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                main()
            if event.type == pygame.KEYDOWN:
                main()


if __name__ == '__main__':
    main()
