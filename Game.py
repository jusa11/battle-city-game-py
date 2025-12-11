import pygame
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_FILL
from MainTank import MainTank
from EnemyTank import EnemyTankSet


class GameSet:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_font = pygame.font.Font(None, 30)
        self.game_score = 0
        self.is_running = True
        self.game_over_text = self.game_font.render('Game over', True, 'white')
        self.game_over_rectangle = self.game_over_text.get_rect()
        self.main_tank = MainTank()
        self.enemy_tanks = pygame.sprite.Group()
        self.destroy_tank_sound = pygame.mixer.Sound(
            file='./sounds/explosion-tank.mp3')

    def init_game(self):
        self.screen.fill(BACKGROUND_FILL)
        game_score_text = self.game_font.render(
            f"Score: {self.game_score}", True, 'white')
        self.screen.blit(game_score_text, (20, 20))

    def run(self):
        # Движение игрока
        self.main_tank.handle_user_input()
        self.main_tank.move(self.main_tank, self.enemy_tanks)
        self.draw_sprite(self.main_tank)

        # Респаун врагов
        while len(self.enemy_tanks) < 2:
            self.spawn_enemy_tanks()

        # Движение врагов
        for enemy_tank in self.enemy_tanks:
            # enemy_tank.handle_user_input()
            enemy_tank.move(self.main_tank, self.enemy_tanks)
            self.draw_sprite(enemy_tank)

        # Движение ракеты
        for rocket in self.main_tank.rockets:
            self.screen.blit(rocket.img, (rocket.x, rocket.y))
            rocket.shot()
            # rocket.update()
            self.draw_sprite(rocket)

        # Попадание ракеты
        hits = pygame.sprite.groupcollide(
            self.main_tank.rockets, self.enemy_tanks, True, True)
        for rocket, enemies in hits.items():
            rocket.shell_explosion(self.screen)
            self.game_score += 150
            self.destroy_tank_sound.play()


    def draw_sprite(self, sprite):
        rotated = pygame.transform.rotate(sprite.img, sprite.angle)
        sprite.rect = rotated.get_rect(center=sprite.rect.center)
        sprite.mask = pygame.mask.from_surface(rotated)
        self.screen.blit(rotated, sprite.rect)


    def spawn_enemy_tanks(self):
        new_enemy_tank = EnemyTankSet()
        self.enemy_tanks.add(new_enemy_tank)


    def over(self):
        game_over_text = self.game_font.render('Game over', True, 'white')
        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.screen.blit(game_over_text, game_over_rectangle)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
