import pygame
from Game import GameSet

pygame.init()
game = GameSet()
clock = pygame.time.Clock()
pygame.display.set_caption("Battle city")

start_game_sound = pygame.mixer.Sound(file='./sounds/start-game.mp3')
start_game_sound.play()


while game.is_running:
    game.init_game()
    game.run()
    pygame.display.update()
    clock.tick(60)

game.over()
