import pygame
from system.movement.RocketMovement import RocketMovement
from system.collisions.ProjectileHit import ProjectileHit
from system.animations.RocketExplosion import RocketExplosion
from configs.config import ROCKET_SPEED


class Projectile(pygame.sprite.Sprite):
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
        self.hit = ProjectileHit(self.rect)
        self.explosion_anim = RocketExplosion()
        self.possible_shot_directions = {
            0: lambda: setattr(self, 'y', self.y - ROCKET_SPEED),
            -90: lambda: setattr(self, 'x', self.x + ROCKET_SPEED),
            180: lambda: setattr(self, 'y', self.y + ROCKET_SPEED),
            90: lambda: setattr(self, 'x', self.x - ROCKET_SPEED),
        }


    def update(self, enemies=None, player=None, game_score=None):
        if self.alive:
            self.movement.move(self)
            if self.hit.hit_target(enemies, player):
                if game_score:
                    game_score['score'] += 150
                self.alive = False

        if self.explosion_anim.anim.finished:
            self.kill()


    def draw(self, screen):
        if self.alive:
            rotated = pygame.transform.rotate(self.img, self.angle)
            screen.blit(rotated, self.rect)
        if not self.alive:
            self.explosion_anim.start_anim(screen, self.x, self.y)
