import pygame
from random import randint
from constans import ENEMY_TANK_STEP


class EnemyTankSet:
    def __init__(self, screen_width):
        self.img = pygame.image.load('./images/enemy-tank-easy.png')
        self.width, self.height = self.img.get_size()
        self.x = randint(0, screen_width - self.width)
        self.y = 0

    def move(self):
        self.y  += ENEMY_TANK_STEP