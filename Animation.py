import pygame

class Animation:
    def __init__(self, frames, duration=100):
        self.frames = frames
        self.duration = duration
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now =  pygame.time.get_ticks()

        if now >= self.duration:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0

    def get_image(self):
        return self.frames[self.current_frame]