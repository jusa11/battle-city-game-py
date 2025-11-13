import pygame
from random import randint, choice
from config import ENEMY_TANK_STEP, SCREEN_HEIGHT, SCREEN_WIDTH


class EnemyTankSet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('./images/enemy-tank-easy.png')
        self.width, self.height = self.img.get_size()
        self.x = randint(10, SCREEN_WIDTH - self.width)
        self.y = 10
        self.angle = choice([0, -90, 180, 90])
        self.rect = self.img.get_rect()

    def move(self, screen, tanks_collisions):
        if tanks_collisions:
            return
        elif self.angle == 180:
            self.y += ENEMY_TANK_STEP
        elif self.angle == 0:
            self.y -= ENEMY_TANK_STEP
        elif self.angle == 90:
            self.x -= ENEMY_TANK_STEP
        elif self.angle == -90:
            self.x += ENEMY_TANK_STEP

        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0 or self.y > SCREEN_HEIGHT - self.height - 10 or self.x > SCREEN_WIDTH - self.width - 10 or self.x < 0:
            old_angle = self.angle
            if self.angle == 180:
                possible_angles = [a for a in [
                    0, -90, 90] if a != old_angle]
            if self.angle == 0:
                possible_angles = [a for a in [
                    -90, 180, 90] if a != old_angle]
            if self.angle == 90:
                possible_angles = [a for a in [
                    -90, 180, 0] if a != old_angle]
            if self.angle == -90:
                possible_angles = [a for a in [
                    0, 180, 90] if a != old_angle]

            self.angle = choice(possible_angles)
            new_tank_direction = pygame.transform.rotate(
                self.img, self.angle)
            screen.blit(
                new_tank_direction, (self.x, self.y))
