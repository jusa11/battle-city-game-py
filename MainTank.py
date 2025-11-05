import sys
import pygame
from Rocket import RocketSet
from constans import MAIN_TANK_STEP, SCREEN_WIDTH, SCREEN_HEIGHT


class MainTankSet:
    def __init__(self, screen_width, screen_height, rocket):
        self.img = pygame.image.load('./images/main-tank.png')
        self.width, self.height = self.img.get_size()
        self.x = screen_width / 2 - self.width / 2
        self.y = screen_height - self.height
        self.moving_direction = None,
        self.angle = 0
        self.rocket = rocket
        self.key_to_direction = {
            pygame.K_UP: ('up', 0, (0, -1)),
            pygame.K_DOWN: ('down', 180, (0, 1)),
            pygame.K_RIGHT: ('right', -90, (1, 0)),
            pygame.K_LEFT: ('left', 90, (-1, 0)),
        }

    def control_moving(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_to_direction:
                    direction, angle, _ = self.key_to_direction[event.key]
                    self.angle = angle
                    self.moving_direction = direction
                if event.key == pygame.K_SPACE:
                    self.shot_gun()

            if event.type == pygame.KEYUP:
                if event.key in self.key_to_direction:
                    direction, _, _ = self.key_to_direction[event.key]
                    if self.moving_direction == direction:
                        self.moving_direction = None

    def move(self):
        if not self.moving_direction:
            return

        _, _, (dx, dy) = next((v for k, v in self.key_to_direction.items()
                               if v[0] == self.moving_direction),
                              (None, None, (0, 0)))

        new_x = self.x + dx * MAIN_TANK_STEP
        new_y = self.y + dy * MAIN_TANK_STEP

        if 0 <= new_x <= SCREEN_WIDTH - self.width:
            self.x = new_x
        if  0 <= new_y <= SCREEN_HEIGHT - self.height:
            self.y = new_y


    def shot_gun(self):
        self.rocket.is_fired = True
        print(self.rocket.is_fired)
        self.rocket.x = self.x + self.width / 2 - self.rocket.width / 2
        self.rocket.y = self.y - self.rocket.height