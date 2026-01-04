import pygame
from Tank import Tank
from random import randint, choice
from configs.config import SCREEN_WIDTH
from configs.enemy_tank_config import ENEMY_TANK_IMAGE, ENEMY_TANK_FRAMES
import sys


class EnemyTankSet(Tank):
    def __init__(self):
        super().__init__(ENEMY_TANK_IMAGE, randint(10, SCREEN_WIDTH - 50), 450, ENEMY_TANK_FRAMES, choice([0, -90, 180, 90]))
        self.frame = 0
        self.old_coordinates = self.coordinates
        self.is_shot = False


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
        if self.is_shot:
            self.set_action('fire')


    def update(self):
        self.frame += 1


    def main_logic(self, phase, player_coordinates):
        # if self.is_collision:
        #     possible = [60, 120, 180, 240]
        #     if self.frame % choice(possible) == 0:
        #         self.random_phase()
        #
        #
        #     self.random_phase()

        self.random_shot()

        if phase == 'random':
            self.random_phase()
        if phase  == 'chase':
            if self.coordinates != self.old_coordinates:
                self.chase_phase(player_coordinates)

    def random_shot(self):
        possible = 10
        if self.frame % possible == 0:
            if not self.rocket:
                self.is_shot = True
        else:
            self.is_shot = False


    def random_phase(self):
        possible = [0, -90, 90, 180]
        possible.remove(self.angle)
        self.angle = choice(possible)


    def chase_phase(self, player_coordinates):
        current_player_x, current_player_y = player_coordinates
        current_self_x, current_self_y = self.coordinates

        # Игрок справа-внизу
        if current_self_x < current_player_x and current_self_y < current_player_y:
            possible = [-90, 180]
            self.angle = choice(possible)
        # Игрок слева-внизу
        if current_self_x > current_player_x and current_self_y < current_player_y:
            possible = [90, 180]
            self.angle = choice(possible)
        # Игрок справа-вверху
        if current_self_x > current_player_x and current_self_y > current_player_y:
            possible = [90, 0]
            self.angle = choice(possible)
        # Игрок слева-вверху
        if current_self_x < current_player_x and current_self_y > current_player_y:
            possible = [-90, 0]
            self.angle = choice(possible)
        self.old_coordinates = self.coordinates


    def attack_phase(self):
        pass

# Фаза преследования
# 1. На каждом тайле проверка, есть ли препятствие в виде стен (если кирпичная стена ее можно пробивать)
# 2. Если больше 1 свободного направления, выбор 50 на 50