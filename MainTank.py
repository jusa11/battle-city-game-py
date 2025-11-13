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
        self.moving_direction = 0,
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

    def control_moving(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_to_direction:
                    direction, angle, _ = self.key_to_direction[event.key]
                    self.angle = angle
                    self.moving_direction = direction

                    self.driving_tank_sound.play()
                if event.key == pygame.K_SPACE:
                    self.shot_gun()

            if event.type == pygame.KEYUP:
                self.driving_tank_sound.stop()
                if event.key in self.key_to_direction:
                    direction, _, _ = self.key_to_direction[event.key]
                    if self.moving_direction == direction:
                        self.moving_direction = None

    def move(self):
        if not self.moving_direction:
            return
            # Определение направления движения
        _, _, (dx, dy) = next((v for k, v in self.key_to_direction.items()
                               if v[0] == self.moving_direction),
                              (None, None, (0, 0)))

        new_x = self.x + (dx * MAIN_TANK_STEP)
        new_y = self.y + (dy * MAIN_TANK_STEP)

        # Ограничение выезда за предела экрана
        if 0 <= new_x <= SCREEN_WIDTH - self.width:
            self.x = new_x
            self.rect.x = self.x

        if 0 <= new_y <= SCREEN_HEIGHT - self.height:
            self.y = new_y
            self.rect.y = self.y

    def shot_gun(self):
        if self.angle == 0 or self.angle == 180:
            rocket_x = self.x + self.width / 2 - 3
            rocket_y = self.y + 10
        if self.angle == 90 or self.angle == -90:
            rocket_x = self.x + self.width / 2 - 3
            rocket_y = self.y + 10

        new_rocket = RocketSet(rocket_x, rocket_y, self.angle)
        self.rockets.add(new_rocket)
        self.shot_sound.play()
