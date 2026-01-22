from system.animations.Animation import Animation
from configs.config import TANK_EXPLOSION_FRAMES

class TankExplosion:
    def __init__(self):
        self.explosion_frames = TANK_EXPLOSION_FRAMES
        self.anim = Animation(self.explosion_frames, 100, False)

    def start_anim(self, screen, tank_x, tank_y):
        if self.anim and not self.anim.finished:
            self.anim.update()
            screen.blit(self.anim.get_image(),
                    (tank_x, tank_y))