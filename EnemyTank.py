import pygame
from Tank import Tank
from random import randint, choice
from configs.config import SCREEN_WIDTH
from configs.enemy_tank_config import ENEMY_TANK_IMAGE, ENEMY_TANK_X, ENEMY_TANK_Y
import sys


class EnemyTankSet(Tank):
    def __init__(self):
        super().__init__(ENEMY_TANK_IMAGE, randint(10, SCREEN_WIDTH - 50), 450, choice([0, -90, 180, 90]))

    def handle_ai_input(self, action):
        """Обработка событий от AI"""
        pass



