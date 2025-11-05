import pygame
from constans import ROCKET_SPEED
from random import randint
from constans import SCREEN_WIDTH

class RocketSet:
    def __init__(self):
        self.img = pygame.image.load('./images/rocket.png')
        self.width, self.height = self.img.get_size()
        self.x = 0
        self.y = 0
        self.is_fired = False

    def shot(self):
        self.y -= ROCKET_SPEED
        if self.y <= 0:
            self.is_fired = False
            self.x, self.y = 0, 0

    def knocked_tank(self, enemy_tank, game):
        if (self.is_fired and
                enemy_tank.x < self.x < enemy_tank.x +
                enemy_tank.width - self.width
                and enemy_tank.y < self.y < enemy_tank.y +
                enemy_tank.height - self.height):
            self.is_fired = False
            enemy_tank.x = randint(0, SCREEN_WIDTH - enemy_tank.width)
            enemy_tank.y = 0
            game.game_score += 150