import pygame
from configs.config import  SCREEN_WIDTH, SCREEN_HEIGHT

ENEMY_TANK_STEP = 1
ENEMY_TANK_IMAGE = pygame.image.load('./images/enemy-tank-easy-1.png')
ENEMY_TANK_WIDTH, ENEMY_TANK_HEIGHT = ENEMY_TANK_IMAGE.get_size()
ENEMY_TANK_X = SCREEN_WIDTH / 2 - ENEMY_TANK_WIDTH / 2
ENEMY_TANK_Y = SCREEN_HEIGHT - ENEMY_TANK_HEIGHT
ENEMY_TANK_FRAMES = [
    pygame.image.load('./images/enemy-tank-easy-1.png'),
    pygame.image.load('./images/enemy-tank-easy-2.png')
]