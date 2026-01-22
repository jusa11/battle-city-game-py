import pygame

class Animation:
    def __init__(self, frames, duration=100, loop=True, repeat=None):
        self.frames = frames
        self.duration = duration
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.loop = loop
        self.finished = False
        self.repeat = repeat
        self.laps = 0

    def update(self):
        if self.finished:
            return

        now =  pygame.time.get_ticks()

        if now - self.last_update >= self.duration:
            self.last_update = now
            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                if self.repeat is not None:
                    self.laps += 1

                    if self.laps >= self.repeat:
                        self.current_frame = len(self.frames) - 1
                        self.finished = True
                    else:
                        self.current_frame = 0
                    return
                if self.loop:
                    self.current_frame = 0
                elif not self.repeat:
                    self.current_frame = len(self.frames) - 1
                    self.finished = True

    def get_image(self):
        return self.frames[self.current_frame]