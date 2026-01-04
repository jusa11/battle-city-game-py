import pygame
from MainTank import MainTank
from EnemyTank import EnemyTankSet
from Map import Map
from GameInfo import Info
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT
from random import choice

class GameSet:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = MainTank()
        self.enemies = pygame.sprite.Group()
        self.map = Map()
        self.info = Info()
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
        # Воскрешение
        if not self.player.alive:
            possible = [50, 100, 150, 200]
            if self.timer % choice(possible) == 0:
                self.player.alive = True

        # Движение игрока
        self.player.handle_user_input()
        self.player.move(self.player, self.enemies, self.map)
        self.timer += 1

        self.get_period()

        # Движение врагов
        for enemy in self.enemies:
            enemy.update()
            enemy.move(self.player, self.enemies, self.map)
            enemy.main_logic(self.current_phase, self.player.coordinates)
            enemy.handle_ai_input()

            if enemy.rocket:
                enemy.rocket.move()
                enemy.rocket.hit_rocket(player=self.player)
                print(enemy.rocket)

                if enemy.rocket and enemy.rocket.explosion_anim.finished:
                    enemy.rocket = None

                if enemy.rocket and enemy.rocket.alive:
                    self.map.destruction_brick(enemy.rocket, enemy.shot_direction)


        # Движение ракеты
        if self.player.rocket:
            self.player.rocket.move()
            self.player.rocket.hit_rocket(enemies=self.enemies, game_score=self.info.game_info)

        if self.player.rocket and self.player.rocket.explosion_anim.finished:
            self.player.rocket = None

        # Респаун врагов
        while len(self.enemies) < 1:
            self.spawn_enemy_tanks()

        if self.player.rocket and self.player.rocket.alive:
            self.map.destruction_brick(self.player.rocket, self.player.shot_direction)


    def draw(self):
        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)
            if enemy.rocket:
                enemy.rocket.draw(self.screen)

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
