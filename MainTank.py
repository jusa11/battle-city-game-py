from Entities.Tank.Tank import Tank
from configs.sounds import DRIVING_TANK_SOUND
from configs.main_tank_config import MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES
from Entities.Tank.TankMovement import TankMovement
from InputSystem import InputSystem

class MainTank(Tank):
    def __init__(self):
        super().__init__(MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES)
        self.driving_tank_sound = DRIVING_TANK_SOUND
        self.movement = TankMovement()
        self.control_driving = InputSystem()

    def update(self, context):
        enemies = context['enemies']
        map = context['map']
        timer = context['timer']
        score = context['score']

        self.control_driving.tank_driving(self)
        self.movement.move(self, enemies, map)
        self.resurrection(timer)

        if self.weapon.rocket:
            self.weapon.rocket.update(enemies=enemies, game_score=score)

        if self.weapon.rocket and self.weapon.rocket.explosion.explosion_anim.finished:
            self.weapon.rocket = None

        if self.weapon.rocket and self.weapon.rocket.alive:
            map.destruction_brick(self.weapon.rocket, self.weapon.shot_direction)


    def resurrection(self, timer):
        if not self.alive:
            if timer % 50 == 0:
                self.alive = True
