from Entities.Rocket.Rocket import Rocket
from configs.sounds import SHOT


class TankWeapon():
    def __init__(self):
        super().__init__()
        self.rocket = None
        self.shot_sound = SHOT
        self.shot_direction = None


    def shot_gun(self, data):
        angle = data['angle']
        tank_x = data['tank_x']
        tank_y = data['tank_y']
        tank_width = data['tank_width']
        tank_height = data['tank_height']

        if self.rocket:
            return
        """Выстрел пушки"""
        if angle == 0:
            self.shot_direction = 'bottom'
            rocket_x = tank_x + tank_width // 2 - 4
            rocket_y = tank_y + 15
        elif angle == 180:
            self.shot_direction = 'top'
            rocket_x = tank_x + tank_width // 2 - 4
            rocket_y = tank_y - 15
        elif angle == 90:
            self.shot_direction = 'right'
            rocket_x = tank_x + 15
            rocket_y = tank_y + tank_height // 2 - 4
        elif angle == -90:
            self.shot_direction = 'left'
            rocket_x = tank_x - 15
            rocket_y = tank_y + tank_height // 2 - 4

        new_rocket = Rocket(rocket_x, rocket_y, angle)
        self.rocket = new_rocket
        self.shot_sound.play()
