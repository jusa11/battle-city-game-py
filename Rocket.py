import pygame
from random import randint
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ROCKET_SPEED


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

    def shot(self, screen):
        if self.angle in self.possible_shot_directions:
            self.possible_shot_directions[self.angle]()
            self.rect.x = self.x
            self.rect.y = self.y

            if self.y <= 0 or self.y > SCREEN_HEIGHT - self.explosion_rocket_height or self.x > SCREEN_WIDTH - self.explosion_rocket_width or self.x < 0:
                self.shell_explosion(screen)
                self.kill()

    def knocked_tank(self, enemy_tank, game):
        if (self.is_fired and
                enemy_tank.x < self.x < enemy_tank.x +
                enemy_tank.width - self.width
                and enemy_tank.y < self.y < enemy_tank.y +
                enemy_tank.height - self.height):
            self.is_fired = False
            enemy_tank.x = randint(0, SCREEN_WIDTH - enemy_tank.width)
            enemy_tank.y = 0
            game.game_score += 150
            game.current_enemy_tank_count -= 1
            self.destroy_tank_sound.play()

    def shell_explosion(self, screen):
        print('SHELL IN')
        screen.blit(self.explosion_rocket_img,
                    (self.x, self.y))
