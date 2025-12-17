import pygame
pygame.init()
pygame.mixer.init()
from configs.sounds import load_sounds
load_sounds()
from Game import GameSet
from configs.sounds import START_GAME

game = GameSet()
clock = pygame.time.Clock()
pygame.display.set_caption("Battle city")

start_game_sound = START_GAME
start_game_sound.play()


while True:
    game.screen.fill((17, 17, 17))
    game.update()
    game.draw()
    pygame.display.update()
    clock.tick(60)

