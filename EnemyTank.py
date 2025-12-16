import pygame
from Tank import Tank
from Animation import Animation
from random import randint, choice
from configs.config import SCREEN_WIDTH
from configs.enemy_tank_config import ENEMY_TANK_IMAGE, ENEMY_TANK_FRAMES
import sys


class EnemyTankSet(Tank):
    def __init__(self):
        super().__init__(ENEMY_TANK_IMAGE, randint(10, SCREEN_WIDTH - 50), 450, choice([0, -90, 180, 90]))
        self.frame = 0
        self.tracks = ENEMY_TANK_FRAMES
        self.tracks_anim = Animation(self.tracks, 80)
        self.alive = True

    def update(self):
        self.frame += 1

    def handle_ai_input(self):
        """Обработка событий от ИИ"""
        if self.angle == 0:
            self.set_action(pygame.K_w)
        elif self.angle == 180:
            self.set_action(pygame.K_s)
        elif self.angle == -90:
            self.set_action(pygame.K_d)
        elif self.angle == 90:
            self.set_action(pygame.K_a)

    def main_logic(self):
        if self.is_collision:
            possible = [60, 120, 180, 240]
            if self.frame % choice(possible) == 0:
                self.change_direction()

        elif self.frame % 60 == 0:
            self.change_direction()

    def change_direction(self):
        possible = [0, -90, 90, 180]
        possible.remove(self.angle)
        self.angle = choice(possible)

