import  pygame
from Rocket import RocketSet
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from main_tank_config import MAIN_TANK_STEP, MAIN_TANK_WIDTH, MAIN_TANK_HEIGHT

class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_img, tank_x, tank_y, tank_angle=0):
        super().__init__()
        self.img = tank_img
        self.width, self.height = self.img.get_size()
        self.x = tank_x
        self.y = tank_y
        self.rect = self.img.get_rect(topleft=(int(self.x), int(self.y)))   # координаты
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = tank_angle
        self.direction = None
        self.rockets = pygame.sprite.Group()
        self.key_to_direction = {
            pygame.K_UP: ('up', 0, (0, -1)),
            pygame.K_DOWN: ('down', 180, (0, 1)),
            pygame.K_RIGHT: ('right', -90, (1, 0)),
            pygame.K_LEFT: ('left', 90, (-1, 0)),
        }

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



    def move(self, enemy_tanks):
        if not self.direction:
            return

        # dx / dy
        _, _, (dx, dy) = next(
            (v for k, v in self.key_to_direction.items() if v[0] == self.direction),
            (None, None, (0, 0))
        )

        # сохраняем текущую позицию
        old_rect = self.rect.copy()


        # двигаем
        self.rect.x += dx * MAIN_TANK_STEP
        self.rect.y += dy * MAIN_TANK_STEP
        self.x, self.y = self.rect.topleft

        print(bool(self.rect.colliderect))
        self.out_of_screen_restriction(old_rect)
        self.check_collision(enemy_tanks, old_rect)


    def check_collision(self, enemy_tanks, old_rect):
        """Проверка столкновений с врагами"""
        for enemy in enemy_tanks:
            if self.rect.colliderect(enemy.rect):
                # откат при столкновении
                self.rect = old_rect
                self.x, self.y = old_rect.topleft
                return


    def out_of_screen_restriction(self, old_rect):
        """Не выходить за границы"""
        if not (0 <= self.rect.x <= SCREEN_WIDTH - self.width):
            self.rect.x = old_rect.x
        if not (0 <= self.rect.y <= SCREEN_HEIGHT - self.height):
            self.rect.y = old_rect.y


    def shot_gun(self):
        """Выстрел пушки"""
        if self.angle == 0:
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y - 10
        elif self.angle == 180:
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y + self.height
        elif self.angle == 90:
            rocket_x = self.x - 10
            rocket_y = self.y + self.height // 2 - 4
        elif self.angle == -90:
            rocket_x = self.x + self.width
            rocket_y = self.y + self.height // 2 - 4

        new_rocket = RocketSet(rocket_x, rocket_y, self.angle)
        self.rockets.add(new_rocket)
