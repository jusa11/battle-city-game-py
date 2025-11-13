import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_FILL, ENEMY_TANK_COUNT
from MainTank import MainTankSet
from EnemyTank import EnemyTankSet


class GameSet:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_font = pygame.font.Font(None, 30)
        self.game_score = 0
        self.is_running = True
        self.game_over_text = self.game_font.render('Game over', True, 'white')
        self.game_over_rectangle = self.game_over_text.get_rect()
        self.main_tank = MainTankSet(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.enemy_tanks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.main_tank)
        self.all_rockets = self.main_tank.rockets
        self.tanks_collision = False

    def init(self):
        pygame.display.set_caption("Battle city")
        self.screen.fill(BACKGROUND_FILL)

        game_score_text = self.game_font.render(
            f"Score: {self.game_score}", True, 'white')
        self.screen.blit(game_score_text, (20, 20))

    def run(self):

        self.main_tank.control_moving()
        self.main_tank.move()

        main_tank_move = pygame.transform.rotate(
            self.main_tank.img, self.main_tank.angle)
        self.screen.blit(main_tank_move, (self.main_tank.x, self.main_tank.y))

        tanks_collision = pygame.sprite.groupcollide(
            self.all_sprites, self.enemy_tanks, False, False)

        if tanks_collision:
            self.tanks_collision = True

        if len(self.enemy_tanks) < 4:
            while len(self.enemy_tanks) < 4:
                new_enemy_tank = EnemyTankSet()
                self.enemy_tanks.add(new_enemy_tank)

        for enemy_tank in self.enemy_tanks:
            self.screen.blit(enemy_tank.img, (enemy_tank.x, enemy_tank.y))
            enemy_tank.move(self.screen, tanks_collision)

        for rocket in self.all_rockets:
            self.screen.blit(rocket.img, (rocket.x, rocket.y))
            rocket.shot(self.screen)





        hits = pygame.sprite.groupcollide(
            self.main_tank.rockets, self.enemy_tanks, True, True)

        if hits:
            rocket.shell_explosion(self.screen)
            

    def over(self):
        game_over_text = self.game_font.render('Game over', True, 'white')
        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.screen.blit(game_over_text, game_over_rectangle)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
