import pygame
from Entities.Rocket.RocketMovement import RocketMovement
from Entities.Rocket.RocketHit import RocketHit
from Entities.Rocket.RocketExplosion import RocketExplosion
from configs.config import ROCKET_SPEED


class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.img = pygame.image.load('./images/rocket.png')
        self.rect = self.img.get_rect(topleft=(x, y))
        self.width, self.height = self.img.get_size()
        self.x = x
        self.y = y
        self.angle = angle
        self.alive = True
        self.movement = RocketMovement()
        self.hit = RocketHit(self.rect)
        self.explosion = RocketExplosion()
        self.possible_shot_directions = {
            0: lambda: setattr(self, 'y', self.y - ROCKET_SPEED),
            -90: lambda: setattr(self, 'x', self.x + ROCKET_SPEED),
            180: lambda: setattr(self, 'y', self.y + ROCKET_SPEED),
            90: lambda: setattr(self, 'x', self.x - ROCKET_SPEED),
        }


    def update(self, enemies=None, player=None, game_score=None):
        if self.alive:
            self.movement.move(self)
            self.hit.hit_target(self.alive, enemies, player, game_score)
        if self.explosion.explosion_anim.finished:
            self.kill()


    def draw(self, screen):
        if self.alive:
            rotated = pygame.transform.rotate(self.img, self.angle)
            screen.blit(rotated, self.rect)
        if not self.alive:
            self.explosion.rocket_explosion(screen, self.x, self.y)
