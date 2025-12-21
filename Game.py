import pygame
from MainTank import MainTank
from EnemyTank import EnemyTankSet
from Map import Map
from GameInfo import Info
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT


class GameSet:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = MainTank()
        self.enemies = pygame.sprite.Group()
        self.map = Map()
        self.info = Info()


    def update(self):
        # Движение игрока
        self.player.handle_user_input()
        self.player.move(self.player, self.enemies, self.map, self.screen)

        # Движение врагов
        for enemy in self.enemies:
            enemy.update()
            enemy.main_logic()
            enemy.handle_ai_input()
            enemy.move(self.player, self.enemies, self.map, self.screen)

        # Движение ракеты
        if self.player.rocket:
            self.player.rocket.move()
            self.player.rocket.hit_rocket(self.enemies, self.info.game_info, self.player)

        if self.player.rocket and self.player.rocket.explosion_anim.finished:
            self.player.rocket = None

        # Респаун врагов
        while len(self.enemies) < 1:
            self.spawn_enemy_tanks()
        self.map.destruction_brick(self.player.rocket, self.screen, self.player.shot_direction)


    def draw(self):
        self.map.draw(self.screen)

        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        if self.player.rocket:
            self.player.rocket.draw(self.screen, self.player)

        self.info.show(self.screen)


    def spawn_enemy_tanks(self):
        new_enemy_tank = EnemyTankSet()
        self.enemies.add(new_enemy_tank)


