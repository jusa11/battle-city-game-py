from entities.Tank import Tank
from configs.sounds import DRIVING_TANK_SOUND
from configs.main_tank_config import MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES, MAIN_TANK_STEP
from system.movement.TankMovement import TankMovement
from system.input.PlayerInput import PlayerInput

class MainTank(Tank):
    def __init__(self):
        super().__init__(MAIN_TANK_IMAGE, MAIN_TANK_X, MAIN_TANK_Y, MAIN_TANK_FRAMES)
        self.driving_tank_sound = DRIVING_TANK_SOUND
        self.movement = TankMovement()
        self.control_driving = PlayerInput()
        self.speed = MAIN_TANK_STEP


    def update(self, context):
        self.control_driving.tank_driving(self)
        self.movement.move(self, context)
        self.resurrection(context.timer)
        if self.weapon.rocket:
            self.weapon.rocket.update(enemies=context.enemies, game_score=context.score)

        if self.weapon.rocket and self.weapon.rocket.explosion_anim.anim.finished:
            self.weapon.rocket = None

        if self.weapon.rocket and self.weapon.rocket.alive:
            context.map.destruction_brick(self.weapon.rocket, self.weapon.shot_direction)


    def resurrection(self, timer):
        if not self.alive:
            if timer % 50 == 0:
                self.alive = True
