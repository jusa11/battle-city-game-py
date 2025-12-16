import pygame
from Animation import Animation
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT, ROCKET_SPEED, ROCKET_EXPLOSION_FRAMES


class RocketSet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.img = pygame.image.load('./images/rocket.png')
        self.rect = self.img.get_rect(topleft=(x, y))
        self.width, self.height = self.img.get_size()
        self.x = x
        self.y = y
        self.angle = angle
        self.alive = True
        self.speed = ROCKET_SPEED
        self.explosion_frames = ROCKET_EXPLOSION_FRAMES
        self.explosion_anim = Animation(self.explosion_frames, 30, False)
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

    def destroy(self):
        self.alive = False

    def shot(self):
        if not self.alive:
            return
        if self.angle in self.possible_shot_directions:
            self.possible_shot_directions[self.angle]()
            self.rect.x = self.x
            self.rect.y = self.y

            if self.is_off_screen():
                self.alive = False

    def shell_explosion(self, screen):
        if self.explosion_anim and not self.explosion_anim.finished:
            self.explosion_anim.update()
            screen.blit(self.explosion_anim.get_image(),
                    (self.x, self.y))

    def is_off_screen(self):
        return (self.y < 0 or self.y > SCREEN_HEIGHT - self.height or
                self.x < 0 or self.x > SCREEN_WIDTH - self.width)