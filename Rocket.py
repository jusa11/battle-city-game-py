import pygame
from Animation import Animation
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT, ROCKET_SPEED, ROCKET_EXPLOSION_FRAMES
from configs.sounds import DESTROY_TANK_SOUND


class RocketSet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.img = pygame.image.load('./images/rocket.png')
        self.rect = self.img.get_rect(topleft=(x, y))
        self.width, self.height = self.img.get_size()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = angle
        self.alive = True
        self.destroy_tank_sound = DESTROY_TANK_SOUND
        self.explosion_frames = ROCKET_EXPLOSION_FRAMES
        self.explosion_anim = Animation(self.explosion_frames, 30, False)
        self.explosion_rocket_img = pygame.image.load(
            './images/explosion_rocket.png')
        self.explosion_rocket_width, self.explosion_rocket_height = self.explosion_rocket_img.get_size()
        self.possible_shot_directions = {
            0: lambda: setattr(self, 'y', self.y - ROCKET_SPEED),
            -90: lambda: setattr(self, 'x', self.x + ROCKET_SPEED),
            180: lambda: setattr(self, 'y', self.y + ROCKET_SPEED),
            90: lambda: setattr(self, 'x', self.x - ROCKET_SPEED),
        }

    def move(self):
        if self.alive:
            if self.angle in self.possible_shot_directions:
                self.possible_shot_directions[self.angle]()
                self.rect.x = self.x
                self.rect.y = self.y

                if self.out_of_screen():
                    self.alive = False


    def hit_rocket(self, enemies, game_score):
        """Попадание снаряда"""
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect) and self.alive:
                self.destroy()
                enemy.alive = False
                game_score['score'] += 150
                self.destroy_tank_sound.play()
                break
            if self.explosion_anim.finished:
                self.kill()

    def destroy(self):
        self.alive = False


    def shell_explosion(self, screen):
        if self.explosion_anim and not self.explosion_anim.finished:
            self.explosion_anim.update()
            screen.blit(self.explosion_anim.get_image(),
                    (self.x -22, self.y - 22))

    def out_of_screen(self):
        return (self.y < 0 or self.y > SCREEN_HEIGHT - self.height or
                self.x < 0 or self.x > SCREEN_WIDTH - self.width)


    def draw(self, screen):
        if self.alive:
            rotated = pygame.transform.rotate(self.img, self.angle)
            screen.blit(rotated, self.rect)
        if not self.alive:
            self.shell_explosion(screen)
