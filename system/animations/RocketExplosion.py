from system.animations.Animation import Animation
from configs.config import ROCKET_EXPLOSION_FRAMES


class RocketExplosion:
    def __init__(self):
        self.explosion_frames = ROCKET_EXPLOSION_FRAMES
        self.anim = Animation(self.explosion_frames, 30, False)


    def start_anim(self, screen, rocket_x, rocket_y):
        if self.anim and not self.anim.finished:
            self.anim.update()
            screen.blit(self.anim.get_image(),
                    (rocket_x -22, rocket_y - 22))