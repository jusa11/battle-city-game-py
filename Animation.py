import pygame

class Animation:
    def __init__(self, frames, duration=100, loop=True):
        self.frames = frames
        self.duration = duration
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.loop = loop
        self.finished = False

    def update(self):
        if self.finished:
            return

        now =  pygame.time.get_ticks()

        if now - self.last_update >= self.duration:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                if self.loop:
                    self.current_frame = 0
                else:
                    self.current_frame = len(self.frames) - 1
                    self.finished = True

    def get_image(self):
        return self.frames[self.current_frame]