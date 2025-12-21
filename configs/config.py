import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 832, 832
TILE_SIZE = 64
BACKGROUND_FILL = (17, 17, 17)
ENEMY_TANK_STEP = 3
ROCKET_SPEED = 20
ENEMY_TANK_COUNT = 4
KEY_TO_DIRECTION = {
            pygame.K_w: ('up', 0, (0, -1)),
            pygame.K_s: ('down', 180, (0, 1)),
            pygame.K_d: ('right', -90, (1, 0)),
            pygame.K_a: ('left', 90, (-1, 0)),
        }
ROCKET_EXPLOSION_FRAMES = [
    pygame.image.load('./images/explosion-rocket-1.png'),
    pygame.image.load('./images/explosion-rocket-2.png'),
    pygame.image.load('./images/explosion-rocket-3.png'),
]
TANK_EXPLOSION_FRAMES = [
    pygame.image.load('./images/tank_explosion-1.png'),
    pygame.image.load('./images/tank_explosion-2.png'),
]




