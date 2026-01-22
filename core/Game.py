import pygame
from entities.MainTank import MainTank
from entities.EnemyTank import EnemyTank
from world.Map import Map
from world.GameInfo import Info
from core.GameContext import GameContext
from system.EnemySpawner import EnemySpawner
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT


class GameSet:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = MainTank()
        self.enemies = pygame.sprite.Group()
        self.map = Map()
        self.game_info = Info()
        self.enemy_spawner = EnemySpawner()
        self.timer = 0
        self.current_phase = 'chase'
        self.last_respawn = 0


    def get_period(self):
        print(self.timer)
        if self.timer < 3000:
            self.current_phase = 'random'
            print(self.current_phase)
        if self.timer > 3000 and self.timer < 6000:
            self.current_phase = 'chase'
            print(self.current_phase)
        if self.timer > 6000 and self.timer < 9000:
            self.current_phase = 'attack'
            print(self.current_phase)

        if self.timer > 9000:
            self.timer = 0


    def update(self):
        context = GameContext(self.player, self.enemies, self.map, self.timer, self.game_info.score, self.current_phase)

        self.player.update(context)

        for enemy in self.enemies:
            enemy.update(context)

        self.timer += 1
        self.get_period()

        # Респаун врагов
        if len(self.enemies) < 2:
            if (self.timer - self.last_respawn) > 60:
                self.enemy_spawner.spawn(self.enemies, self.player)
                self.last_respawn = self.timer

        self.enemy_spawner.update(self.screen, self.enemies)


    def draw(self):
        self.player.draw(self.screen)
        if self.player.weapon.rocket:
            self.player.weapon.rocket.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)
            if enemy.weapon.rocket:
                enemy.weapon.rocket.draw(self.screen)

        self.map.draw(self.screen)

        self.game_info.show(self.screen)
        # self.draw_grid(self.screen)


    def draw_grid(self, screen, grid_size=64, color=(255, 255, 255)):
        """Отрисовка сетки на карте 64х64"""
        width, height = screen.get_size()

        for x in range(0, width, grid_size):
            pygame.draw.line(screen, color, (x, 0), (x, height), 1)

        for y in range(0, height, grid_size):
            pygame.draw.line(screen, color, (0, y), (width, y), 1)
