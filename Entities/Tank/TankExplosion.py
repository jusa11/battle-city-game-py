from Animation import Animation
from configs.config import TANK_EXPLOSION_FRAMES

class TankExplosion:
    def __init__(self):
        self.explosion_frames = TANK_EXPLOSION_FRAMES
        self.explosion_anim = Animation(self.explosion_frames, 100, False)

    def tank_explosion(self, screen, tank_x, tank_y):
        if self.explosion_anim and not self.explosion_anim.finished:
            self.explosion_anim.update()
            screen.blit(self.explosion_anim.get_image(),
                    (tank_x, tank_y))