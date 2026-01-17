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
        self.game_info = Info()
        self.timer = 0
        self.current_phase = None


    def get_period(self):
        # if self.timer < 300:
        #     self.current_phase = 'random'
        #     print(self.current_phase)
        if self.timer > 0 and self.timer < 60000:
            self.current_phase = 'chase'
        # if self.timer > 600 and self.timer < 900:
        #     self.current_phase = 'attack'
        #     print(self.current_phase)

        if self.timer > 900:
            self.timer = 0


    def update(self):
        context = {
            'player': self.player,
            'enemies': self.enemies,
            'map': self.map,
            'timer': self.timer,
            'score': self.game_info.score,
            'current_phase': self.current_phase,

        }

        self.player.update(context)

        for enemy in self.enemies:
            enemy.update(context)

        self.timer += 1
        self.get_period()

        # Респаун врагов
        while len(self.enemies) < 2:
            self.spawn_enemy_tanks()


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


    def spawn_enemy_tanks(self):
        new_enemy_tank = EnemyTankSet()
        self.enemies.add(new_enemy_tank)


    # def draw_grid(self, screen, grid_size=64, color=(255, 255, 255)):
    #     """Отрисовка сетки на карте 64х64"""
    #     width, height = screen.get_size()
    #
    #     for x in range(0, width, grid_size):
    #         pygame.draw.line(screen, color, (x, 0), (x, height), 1)
    #
    #     for y in range(0, height, grid_size):
    #         pygame.draw.line(screen, color, (0, y), (width, y), 1)
