import pygame
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT, ROCKET_SPEED


class RocketSet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.img = pygame.image.load('./images/rocket.png')
        self.rect = self.img.get_rect()
        self.width, self.height = self.img.get_size()
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = ROCKET_SPEED
        self.destroy_tank_sound = pygame.mixer.Sound(
            file='./sounds/explosion-tank.mp3')
        self.explosion_rocket_img = pygame.image.load(
            './images/explosion_rocket.png')
        self.explosion_rocket_width, self.explosion_rocket_height = self.explosion_rocket_img.get_size()
        self.possible_shot_directions = {
            0: lambda: setattr(self, 'y', self.y - ROCKET_SPEED),
            -90: lambda: setattr(self, 'x', self.x + ROCKET_SPEED),
            180: lambda: setattr(self, 'y', self.y + ROCKET_SPEED),
            90: lambda: setattr(self, 'x', self.x - ROCKET_SPEED),
        }

    def shot(self):
        if self.angle in self.possible_shot_directions:
            self.possible_shot_directions[self.angle]()
            self.rect.x = self.x
            self.rect.y = self.y

            if self.is_off_screen():
                self.kill()

    def shell_explosion(self, screen):
        screen.blit(self.explosion_rocket_img,
                    (self.x, self.y))

    def is_off_screen(self):
        return (self.y < 0 or self.y > SCREEN_HEIGHT - self.height or
                self.x < 0 or self.x > SCREEN_WIDTH - self.width)