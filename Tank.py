import  pygame
from Rocket import RocketSet
from Animation import Animation
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT,KEY_TO_DIRECTION, TANK_EXPLOSION_FRAMES, TILE_SIZE
from configs.main_tank_config import MAIN_TANK_STEP
from configs.sounds import SHOT


class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_img, tank_x, tank_y, tracks, tank_angle=0):
        super().__init__()
        self.img = tank_img
        self.width, self.height = self.img.get_size()
        self.x = tank_x
        self.y = tank_y
        self.rect = self.img.get_rect(topleft=(int(self.x), int(self.y)))
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = tank_angle
        self.alive = True
        self.direction = None
        self.rocket = None
        self.is_collision = None
        self.shot_sound = SHOT
        self.key_to_direction = KEY_TO_DIRECTION
        self.tracks = tracks
        self.tracks_anim = Animation(self.tracks, 10)
        self.explosion_frames = TANK_EXPLOSION_FRAMES
        self.explosion_anim = Animation(self.explosion_frames, 100, False)
        self.shot_direction = None
        self.old_direction = None
        self.coordinates = None


    def set_action(self, action, is_key_up=False):
        if action == 'fire':
            self.shot_gun()

        if action in self.key_to_direction:
            direction, angle, _ = self.key_to_direction[action]
            self.direction = direction
            self.angle = angle

        if is_key_up and action in self.key_to_direction:
            direction, _, _ = self.key_to_direction[action]
            if self.direction == direction:
                self.direction = None

    def move(self, main_tank, enemy_tanks, map):
        _, _, (dx, dy) = next(
            (v for v in self.key_to_direction.values() if v[0] == self.direction),
            (None, None, (0, 0))
        )

        old_rect = self.rect.copy()

        if self.direction != self.old_direction:
            if self.direction in ['left', 'right']:
                self.rect.y = round(self.rect.y / TILE_SIZE) * TILE_SIZE
            elif self.direction in ['up', 'down']:
                self.rect.x = round(self.rect.x / TILE_SIZE) * TILE_SIZE

        self.old_direction = self.old_direction

        self.rect.x += dx * MAIN_TANK_STEP
        self.rect.y += dy * MAIN_TANK_STEP

        self.check_collision(main_tank, enemy_tanks, map, old_rect)
        self.out_of_screen(old_rect)

        self.x, self.y = self.rect.topleft
        self.coordinates = (round(self.rect.x / TILE_SIZE), round(self.rect.y / TILE_SIZE))


    def check_collision(self, main_tank, enemy_tanks, map, old_rect):
        # стены
        if pygame.sprite.spritecollide(self, map.tiles, False, pygame.sprite.collide_mask):
            self.rect = old_rect
            self.is_collision = True
            return

        # враги
        for enemy in enemy_tanks:
            if enemy is not self and self.rect.colliderect(enemy.rect):
                self.rect = old_rect
                self.is_collision = True
                return

        # главный танк
        if self is not main_tank and self.rect.colliderect(main_tank.rect):
            self.rect = old_rect
            self.is_collision = True
            return


    def out_of_screen(self, old_rect):
        """Не выходить за границы"""
        # границы экрана
        if not (0 <= self.rect.x <= SCREEN_WIDTH - self.rect.width and
                0 <= self.rect.y <= SCREEN_HEIGHT - self.rect.height):
            self.rect = old_rect
            self.is_collision = True
            return


    def shot_gun(self):
        if self.rocket:
            return
        """Выстрел пушки"""
        if self.angle == 0:
            self.shot_direction = 'bottom'
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y + 15
        elif self.angle == 180:
            self.shot_direction = 'top'
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y - 15
        elif self.angle == 90:
            self.shot_direction = 'right'
            rocket_x = self.x + 15
            rocket_y = self.y + self.height // 2 - 4
        elif self.angle == -90:
            self.shot_direction = 'left'
            rocket_x = self.x - 15
            rocket_y = self.y + self.height // 2 - 4

        new_rocket = RocketSet(rocket_x, rocket_y, self.angle)
        self.rocket = new_rocket
        self.shot_sound.play()


    def tank_explosion(self, screen):
        if self.explosion_anim and not self.explosion_anim.finished:
            self.explosion_anim.update()
            screen.blit(self.explosion_anim.get_image(),
                    (self.x, self.y))


    def draw(self, screen):
        if self.alive:
            rotated = pygame.transform.rotate(self.img, self.angle)
            screen.blit(rotated, self.rect)

            if self.tracks_anim and self.direction:
                self.tracks_anim.update()
                img = self.tracks_anim.get_image()
                rotated = pygame.transform.rotate(img, self.angle)
                screen.blit(rotated,
                            (self.x, self.y))
        else:
            self.tank_explosion(screen)
            if self.explosion_anim.finished:
                self.kill()

