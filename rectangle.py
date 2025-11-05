import sys

import pygame

pygame.init()
screen_width, screen_height = 800, 600
rect_height, rect_width = 200, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2
STEP = 100


screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My pygame")



while True:
    screen.fill((105, 105, 105))
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - STEP - rect_height:
                rect_y += STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - STEP - rect_width:
                rect_x += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP