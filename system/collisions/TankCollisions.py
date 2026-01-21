import pygame
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT

class TankCollisions():
    def __init__(self):
        super().__init__()

    def check_collision(self, tank, enemies, map, player):
        # За границы поля
        if not (0 <= tank.rect.x <= SCREEN_WIDTH - tank.rect.width and
                0 <= tank.rect.y <= SCREEN_HEIGHT - tank.rect.height):
            tank.rect = tank.old_rect
            tank.is_collision = True
            return

        # стены
        if pygame.sprite.spritecollide(tank, map.tiles, False, pygame.sprite.collide_mask):
            tank.rect = tank.old_rect
            tank.is_collision = True
            return

        # враги
        for enemy in enemies:
            if enemy is not tank and tank.rect.colliderect(enemy.rect):
                tank.rect = tank.old_rect
                tank.is_collision = True
                return

        # игрок с врагами
        if player and tank is not player and tank.rect.colliderect(player.rect):
            tank.rect = tank.old_rect
            tank.is_collision = True
            return

