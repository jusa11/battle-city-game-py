import pygame
from random import randint, choice
from config import ENEMY_TANK_STEP, SCREEN_HEIGHT, SCREEN_WIDTH


class EnemyTankSet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('./images/enemy-tank-easy.png')
        self.width, self.height = self.img.get_size()
        spawn_x = randint(10, SCREEN_WIDTH - self.width)
        spawn_y = 450
        self.rect = self.img.get_rect(topleft=(spawn_x, spawn_y))
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = choice([0, -90, 180, 90])
        self.tanks_collisions = False


    def move(self, main_tank, enemy_tanks):

        old_pos = self.rect.topleft

        # Движение
        if self.angle == 180:
            self.rect.y += ENEMY_TANK_STEP
        elif self.angle == 0:
            self.rect.y -= ENEMY_TANK_STEP
        elif self.angle == 90:
            self.rect.x -= ENEMY_TANK_STEP
        elif self.angle == -90:
            self.rect.x += ENEMY_TANK_STEP

        # Если упёрся в край — меняем направление
        if (
            self.rect.x < 0 or
            self.rect.x > SCREEN_WIDTH - self.width or
            self.rect.y < 0 or
            self.rect.y > SCREEN_HEIGHT - self.height
        ):
            self.rect.topleft = old_pos
            self.change_direction()


        # Проверка столкновения врага с главным танком
        if pygame.sprite.collide_mask(self, main_tank):
            self.rect.topleft = old_pos
            self.change_direction()
            return


        for enemy_tank in enemy_tanks:
            if enemy_tank is not self:
                if pygame.sprite.collide_mask(self, enemy_tank):
                    self.rect.topleft = old_pos
                    self.change_direction()
                    return


    def backstep(self):
        if self.angle == 180:
            self.rect.y -= ENEMY_TANK_STEP
        elif self.angle == 0:
            self.rect.y += ENEMY_TANK_STEP
        elif self.angle == 90:
            self.rect.x += ENEMY_TANK_STEP
        elif self.angle == -90:
            self.rect.x -= ENEMY_TANK_STEP


    def change_direction(self):
        possible = [0, -90, 90, 180]
        possible.remove(self.angle)
        self.angle = choice(possible)

