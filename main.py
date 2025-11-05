import pygame
from Game import GameSet

pygame.init()
game = GameSet()

while game.is_running:
    game.init()
    game.run()
    pygame.display.update()

game.over()
