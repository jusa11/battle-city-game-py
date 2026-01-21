import pygame
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT

MAIN_TANK_STEP = 3
MAIN_TANK_IMAGE = pygame.image.load('./images/main-tank-1.png')
MAIN_TANK_WIDTH, MAIN_TANK_HEIGHT = MAIN_TANK_IMAGE.get_size()
MAIN_TANK_X = SCREEN_WIDTH // 3 - MAIN_TANK_WIDTH / 2
MAIN_TANK_Y = SCREEN_HEIGHT - MAIN_TANK_HEIGHT
MAIN_TANK_FRAMES = [
    pygame.image.load('./images/main-tank-1.png'),
    pygame.image.load('./images/main-tank-2.png')
]