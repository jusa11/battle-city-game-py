import sys
import pygame
from Rocket import RocketSet
from config import MAIN_TANK_STEP, SCREEN_WIDTH, SCREEN_HEIGHT


class MainTankSet(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.img = pygame.image.load('./images/main-tank.png')
        self.width, self.height = self.img.get_size()
        self.x = screen_width / 2 - self.width / 2
        self.y = screen_height - self.height
        self.rect = self.img.get_rect()
        self.rect.topleft = (int(self.x), int(self.y))
        self.moving_direction = None
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = 0
        self.rockets = pygame.sprite.Group()
        self.driving_tank_sound = pygame.mixer.Sound(
            file='./sounds/ride-tank.mp3')
        self.shot_sound = pygame.mixer.Sound(file='./sounds/shot-gun.mp3')
        self.key_to_direction = {
            pygame.K_UP: ('up', 0, (0, -1)),
            pygame.K_DOWN: ('down', 180, (0, 1)),
            pygame.K_RIGHT: ('right', -90, (1, 0)),
            pygame.K_LEFT: ('left', 90, (-1, 0)),
        }

    def control_moving(self, game):
        """Обработка событий нажатия на клавиши. Изменение направления. Стрельба"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_to_direction:
                    direction, angle, _ = self.key_to_direction[event.key]
                    # выбор угла и направления
                    self.angle = angle
                    self.moving_direction = direction

                    self.driving_tank_sound.play()
                if event.key == pygame.K_SPACE:
                    self.shot_gun(game)

            if event.type == pygame.KEYUP:
                self.driving_tank_sound.stop()
                if event.key in self.key_to_direction:
                    direction, _, _ = self.key_to_direction[event.key]
                    if self.moving_direction == direction:
                        self.moving_direction = None

    def move(self, enemy_tanks):
        if not self.moving_direction:
            return

        # dx / dy
        _, _, (dx, dy) = next(
            (v for k, v in self.key_to_direction.items() if v[0] == self.moving_direction),
            (None, None, (0, 0))
        )

        # сохраняем текущую позицию
        old_rect = self.rect.copy()

        # двигаем
        self.rect.x += dx * MAIN_TANK_STEP
        self.rect.y += dy * MAIN_TANK_STEP
        self.x, self.y = self.rect.topleft

        # не выходить за границы
        if not (0 <= self.rect.x <= SCREEN_WIDTH - self.width):
            self.rect.x = old_rect.x
        if not (0 <= self.rect.y <= SCREEN_HEIGHT - self.height):
            self.rect.y = old_rect.y

        # проверка столкновений с врагами
        for enemy in enemy_tanks:
            print(self.rect.colliderect(enemy.rect))
            if self.rect.colliderect(enemy.rect):
                print(self.rect.colliderect(enemy.rect))
                # откат при столкновении
                self.rect = old_rect
                self.x, self.y = old_rect.topleft
                return

    def shot_gun(self, game):
        if self.angle == 0:
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y - 10
        elif self.angle == 180:
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y + self.height
        elif self.angle == 90:
            rocket_x = self.x - 10
            rocket_y = self.y + self.height // 2 - 4
        elif self.angle == -90:
            rocket_x = self.x + self.width
            rocket_y = self.y + self.height // 2 - 4

        new_rocket = RocketSet(rocket_x, rocket_y, self.angle)
        self.rockets.add(new_rocket)
        game.main_tank.rockets.add(new_rocket)
        self.shot_sound.play()
