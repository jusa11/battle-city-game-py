import pygame
import sys
from constans import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_FILL
from MainTank import MainTankSet
from EnemyTank import EnemyTankSet
from Rocket import RocketSet

class GameSet:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_font = pygame.font.Font(None, 30)
        self.game_score = 0
        self.is_running = True
        self.game_over_text = self.game_font.render('Game over', True, 'white')
        self.game_over_rectangle = self.game_over_text.get_rect()
        self.rocket = RocketSet()
        self.main_tank = MainTankSet(SCREEN_WIDTH, SCREEN_HEIGHT, self.rocket)
        self.enemy_tank = EnemyTankSet(SCREEN_WIDTH)

    def init(self):
        pygame.display.set_caption("Battle city")
        main_tank_move = pygame.transform.rotate(self.main_tank.img, self.main_tank.angle)
        self.screen.fill(BACKGROUND_FILL)
        self.screen.blit(main_tank_move, (self.main_tank.x, self.main_tank.y))
        self.screen.blit(self.enemy_tank.img, (self.enemy_tank.x, self.enemy_tank.y))

        if self.rocket.is_fired:
            self.screen.blit(self.rocket.img, (self.rocket.x, self.rocket.y))

        game_score_text = self.game_font.render(f"Score: {self.game_score}", True, 'white')
        self.screen.blit(game_score_text, (20, 20))

    def run(self):
        self.main_tank.control_moving()
        self.main_tank.move()
        self.enemy_tank.move()
        self.rocket.knocked_tank(self.enemy_tank, self)

        if self.rocket.is_fired:
            self.rocket.shot()


        if self.enemy_tank.y > self.main_tank.y:
            self.is_running = False


    def over(self):
        game_over_text = self.game_font.render('Game over', True, 'white')
        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.screen.blit(game_over_text, game_over_rectangle)
        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()



