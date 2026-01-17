import pygame

class Info:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.score = {'score': 0}

    def show(self, screen):
        text_info = self.font.render(
            f"Score: {self.score['score']}", True, 'white')
        screen.blit(text_info, (20, 20))