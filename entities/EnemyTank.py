from entities.Tank import Tank
from system.input.AiInput import AiInput
from random import randint, choice
from configs.config import SCREEN_WIDTH, POSSIBLE_DIRECTIONS
from configs.enemy_tank_config import ENEMY_TANK_IMAGE, ENEMY_TANK_FRAMES, ENEMY_TANK_STEP
from system.movement.TankMovement import TankMovement
from system.EnemyAI.EnemyAI import EnemyAI

class EnemyTank(Tank):
    def __init__(self, spawn_x):
        super().__init__(ENEMY_TANK_IMAGE, spawn_x, 0, ENEMY_TANK_FRAMES, choice([0, -90, 180, 90]))
        self.frame = 0
        self.old_coordinates = self.coordinates
        self.is_shot = False
        self.control_driving = AiInput()
        self.movement = TankMovement()
        self.possible_directions = POSSIBLE_DIRECTIONS
        self.speed = ENEMY_TANK_STEP
        self.think_cooldown = 0
        self.last_good_angle = None
        self.ai_manager = EnemyAI()


    def update(self, context):
        self.frame += 1
        self.think_cooldown -= 1

        self.control_driving.ai_driving(self)
        moved = self.movement.move(self, context)

        if moved:
            self.last_good_angle = self.angle

        if context.phase == 'random':
            if not moved and self.think_cooldown <= 0:
                self.ai_manager.random_moving(self)
                self.think_cooldown = 60

        if context.phase == 'chase':
            if not moved and self.think_cooldown <= 0:
                self.ai_manager.attack_moving(self, context.player.coordinates, context.map)
                self.think_cooldown = 60

        if context.phase == 'attack':
            if not moved and self.think_cooldown <= 0:
                self.ai_manager.attack_moving(self, (6, 12), context.map)
                self.think_cooldown = 60

        self.ai_manager.shooting(self)

        if self.weapon.rocket:
            self.weapon.rocket.update(player=context.player)

            if self.weapon.rocket and self.weapon.rocket.explosion_anim.anim.finished:
                self.weapon.rocket = None

            if self.weapon.rocket and self.weapon.rocket.alive:
                context.map.destruction_brick(self.weapon.rocket, self.weapon.shot_direction)
