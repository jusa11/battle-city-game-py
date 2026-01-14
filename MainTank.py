import sys
import pygame
from Entities.Tank import Tank
from configs.sounds import DRIVING_TANK_SOUND
from configs.main_tank_config import MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES
from Entities.Movement import Movement



class MainTank(Tank):
    def __init__(self):
        super().__init__(MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES)
        self.driving_tank_sound = DRIVING_TANK_SOUND
        self.movement = Movement()

    def update(self, context):
        enemies = context['enemies']
        map = context['map']
        timer = context['timer']
        score = context['score']


        self.handle_user_input()
        self.movement.move(self, enemies, map)
        self.resurrection(timer)


        if self.weapon.rocket:
            self.weapon.rocket.move()
            self.weapon.rocket.hit_rocket(enemies=enemies, game_score=score)

        if self.weapon.rocket and self.weapon.rocket.explosion_anim.finished:
            self.weapon.rocket = None

        if self.weapon.rocket and self.weapon.rocket.alive:
            map.destruction_brick(self.weapon.rocket, self.weapon.shot_direction)


    def handle_user_input(self):
        """Обработка ввода"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.set_action('fire')
                else:
                    self.set_action(event.key)
                    self.driving_tank_sound.play()

            if event.type == pygame.KEYUP:
                self.driving_tank_sound.stop()
                if event.key in self.key_to_direction:
                    direction, _, _ = self.key_to_direction[event.key]
                    if self.direction == direction:
                        self.direction = None

    def resurrection(self, timer):
        if not self.alive:
            if timer % 50 == 0:
                self.alive = True
