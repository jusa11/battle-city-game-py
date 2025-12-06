import sys
import pygame
from Rocket import RocketSet
from config import MAIN_TANK_STEP, SCREEN_WIDTH, SCREEN_HEIGHT


class MainTankSet(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.img = pygame.image.load('./images/main-tank.png')
        self.width, self.height = self.img.get_size()
        self.x = screen_width / 2 - self.width / 2
        self.y = screen_height - self.height
        self.rect = self.img.get_rect()
        self.rect.topleft = (int(self.x), int(self.y))
        self.moving_direction = None
        self.mask = pygame.mask.from_surface(self.img)
        self.angle = 0
        self.rockets = pygame.sprite.Group()
        self.driving_tank_sound = pygame.mixer.Sound(
            file='./sounds/ride-tank.mp3')
        self.shot_sound = pygame.mixer.Sound(file='./sounds/shot-gun.mp3')
        self.key_to_direction = {
            pygame.K_UP: ('up', 0, (0, -1)),
            pygame.K_DOWN: ('down', 180, (0, 1)),
            pygame.K_RIGHT: ('right', -90, (1, 0)),
            pygame.K_LEFT: ('left', 90, (-1, 0)),
        }

    def control_moving(self, game):
        """Обработка событий нажатия на клавиши. Изменение направления. Стрельба"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_to_direction:
                    direction, angle, _ = self.key_to_direction[event.key]
                    # выбор угла и направления
                    self.angle = angle
                    self.moving_direction = direction

                    self.driving_tank_sound.play()
                if event.key == pygame.K_SPACE:
                    self.shot_gun(game)

            if event.type == pygame.KEYUP:
                self.driving_tank_sound.stop()
                if event.key in self.key_to_direction:
                    direction, _, _ = self.key_to_direction[event.key]
                    if self.moving_direction == direction:
                        self.moving_direction = None

    def move(self, enemy_tanks):
        """Перемещение танка по игровому полю"""
        if not self.moving_direction:
            return

        # Получаем dx / dy
        _, _, (dx, dy) = next((v for k, v in self.key_to_direction.items()
                               if v[0] == self.moving_direction),
                              (None, None, (0, 0)))

        # Куда хотим поехать
        next_rect = self.rect.move(dx * MAIN_TANK_STEP, dy * MAIN_TANK_STEP)

        # Флаги блокировки направления
        block_x = False
        block_y = False


        # Проверяем — будет ли столкновение
        for enemy in enemy_tanks:
            if next_rect.colliderect(enemy.rect):
                print('main-left', self.rect.left)
                print('enemy-right', enemy.rect.right)
                print('main-right', self.rect.right)
                print('enemy-left', enemy.rect.left)
                # Проверка по X (перекрытие по горизонтали)
                if (self.rect.left <= enemy.rect.right or
                        self.rect.right >= enemy.rect.left):
                    block_x = True
                    print('Block_X is true')


                # Проверка по Y (перекрытие по вертикали)
                if (self.rect.bottom >= enemy.rect.top or
                        self.rect.top <= enemy.rect.bottom):
                    block_y = True
                    print('Block_Y is true')
                    print('main-bottom', self.rect.bottom)
                    print('enemy-top', enemy.rect.top)
                    print('main-top', self.rect.top)
                    print('enemy-bottom', enemy.rect.bottom)



        if not block_x:
            new_x = self.x + dx * MAIN_TANK_STEP
            if 0 <= new_x <= SCREEN_WIDTH - self.width:
                self.x = new_x
                self.rect.x = self.x

        if not block_y:
            new_y = self.y + dy * MAIN_TANK_STEP
            if 0 <= new_y <= SCREEN_HEIGHT - self.height:
                self.y = new_y
                self.rect.y = self.y


    def shot_gun(self, game):
        if self.angle == 0:  # вверх
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y - 10
        elif self.angle == 180:  # вниз
            rocket_x = self.x + self.width // 2 - 4
            rocket_y = self.y + self.height
        elif self.angle == 90:  # влево
            rocket_x = self.x - 10
            rocket_y = self.y + self.height // 2 - 4
        elif self.angle == -90:  # вправо
            rocket_x = self.x + self.width
            rocket_y = self.y + self.height // 2 - 4

        new_rocket = RocketSet(rocket_x, rocket_y, self.angle)
        self.rockets.add(new_rocket)
        game.main_tank.rockets.add(new_rocket)
        self.shot_sound.play()
