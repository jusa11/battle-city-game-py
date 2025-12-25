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
        self.player.move(self.player, self.enemies, self.map)


        # Движение врагов
        for enemy in self.enemies:
            enemy.update()
            enemy.main_logic()
            enemy.handle_ai_input()
            enemy.move(self.player, self.enemies, self.map)


        # Движение ракеты
        if self.player.rocket:
            self.player.rocket.move()
            self.player.rocket.hit_rocket(self.enemies, self.info.game_info)

        if self.player.rocket and self.player.rocket.explosion_anim.finished:
            self.player.rocket = None

        # Респаун врагов
        while len(self.enemies) < 3:
            self.spawn_enemy_tanks()

        if self.player.rocket and self.player.rocket.alive:
            self.map.destruction_brick(self.player.rocket, self.player.shot_direction)



    def draw(self):
        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        self.map.draw(self.screen)
        if self.player.rocket:
            self.player.rocket.draw(self.screen)

        self.info.show(self.screen)
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
