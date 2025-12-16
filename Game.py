import pygame
from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_FILL
from MainTank import MainTank
from EnemyTank import EnemyTankSet
from Map import Map


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
        self.map = Map()
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
        self.main_tank.move(self.main_tank, self.enemy_tanks, self.map)
        self.draw_sprite(self.main_tank)

        self.map.draw_map(self.screen)

        self.map.destruction_brick(self.main_tank.rocket, self.screen)

        # Респаун врагов
        while len(self.enemy_tanks) < 4:
            self.spawn_enemy_tanks()

        # Движение врагов
        for enemy_tank in self.enemy_tanks:
            enemy_tank.update()
            enemy_tank.main_logic()
            enemy_tank.handle_ai_input()
            enemy_tank.move(self.main_tank, self.enemy_tanks, self.map)
            if enemy_tank.alive:
                self.draw_sprite(enemy_tank)
            else:
                enemy_tank.tank_explosion(self.screen)
                if enemy_tank.explosion_anim.finished:
                    enemy_tank.kill()

        # Движение ракеты
        if self.main_tank.rocket and self.main_tank.rocket.alive:
            self.screen.blit(self.main_tank.rocket.img, (self.main_tank.rocket.x, self.main_tank.rocket.y))
            self.main_tank.rocket.shot()
            self.draw_sprite(self.main_tank.rocket)

        # Попадание ракеты
        rocket = self.main_tank.rocket

        if rocket:
            for enemy in self.enemy_tanks:
                if rocket.rect.colliderect(enemy.rect) and rocket.alive:
                    rocket.destroy()  # 🔥 ВАЖНО
                    # enemy.kill()
                    enemy.alive = False
                    self.game_score += 150
                    self.destroy_tank_sound.play()
                    break

        # отрисовка взрыва
        if self.main_tank.rocket and not self.main_tank.rocket.alive:
            self.main_tank.rocket.shell_explosion(self.screen)
            self.main_tank.tank_explosion(self.screen)
            if self.main_tank.rocket.explosion_anim.finished:
                self.main_tank.rocket = None


    def draw_sprite(self, sprite):
        image = sprite.img

        # анимация гусениц
        if hasattr(sprite, 'tracks_anim') and sprite.direction:
            image = sprite.tracks_anim.get_image()

        rotated = pygame.transform.rotate(image, sprite.angle)
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
