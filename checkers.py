import pygame
import sys
from game import Game


def main():
    game = Game()
    game.player1.turn = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                tile = game.get_tile(pos)



if __name__ == '__main__':
    main()
