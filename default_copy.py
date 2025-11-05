import pygame
import sys
from random import randint

pygame.init()
game_font = pygame.font.Font(None, 30)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle city")
background_fill = (17, 17, 17)
STEP = 0.2
ENEMY_STEP = 0.03
ROCKET_SPEED = 0.2
main_tank_angle = 0
is_fired_rocket = False
game_score = 0

main_tank_img = pygame.image.load('./images/main-tank.png')
main_tank_width, main_tank_height = main_tank_img.get_size()
rocket_img = pygame.image.load('./images/rocket.png')
rocket_width, rocket_height = rocket_img.get_size()
enemy_tank_img = pygame.image.load('./images/enemy-tank-easy.png')
enemy_tank_width, enemy_tank_height = enemy_tank_img.get_size()

main_tank_x = screen_width / 2 - main_tank_width / 2
main_tank_y = screen_height - main_tank_height
enemy_tank_x = randint(0, screen_width - enemy_tank_width)
enemy_tank_y = 0


main_tank_is_moving_left, main_tank_is_moving_right = False, False
main_tank_is_moving_down, main_tank_is_moving_up = False, False

game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_tank_angle = 0
                main_tank_is_moving_up = True
            if event.key == pygame.K_DOWN:
                main_tank_angle = 180
                main_tank_is_moving_down = True
            if event.key == pygame.K_RIGHT:
                main_tank_is_moving_right = True
                main_tank_angle = -90
            if event.key == pygame.K_LEFT:
                main_tank_angle = 90
                main_tank_is_moving_left = True

            if event.key == pygame.K_SPACE:
                is_fired_rocket = True
                rocket_x = main_tank_x + main_tank_width / 2 - rocket_width / 2
                rocket_y = main_tank_y - rocket_height


        if event.type == pygame.KEYUP:
                main_tank_is_moving_left = False
                main_tank_is_moving_right = False
                main_tank_is_moving_up = False
                main_tank_is_moving_down = False

    if is_fired_rocket:
        rocket_y -= ROCKET_SPEED
    if is_fired_rocket and rocket_y <= 0:
        is_fired_rocket = False
        rocket_y = main_tank_y - rocket_height

    if main_tank_is_moving_left and main_tank_x >= STEP:
        main_tank_x -= STEP

    if main_tank_is_moving_right and main_tank_x <= screen_width - STEP - main_tank_width:
        main_tank_x += STEP

    if main_tank_is_moving_down and main_tank_y <= screen_height - STEP - main_tank_height:
        main_tank_y += STEP

    if main_tank_is_moving_up and main_tank_y >= STEP:
        main_tank_y -= STEP

    enemy_tank_y += ENEMY_STEP

    main_tank_move = pygame.transform.rotate(main_tank_img, main_tank_angle)
    screen.fill(background_fill)
    screen.blit(main_tank_move, (main_tank_x, main_tank_y))
    screen.blit(enemy_tank_img, (enemy_tank_x, enemy_tank_y))

    if is_fired_rocket:
        screen.blit(rocket_img, (rocket_x, rocket_y))

    game_score_text = game_font.render(f"Score: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()

    if enemy_tank_y > main_tank_y:
        game_is_running = False

    if (is_fired_rocket and
            enemy_tank_x < rocket_x < enemy_tank_x +
            enemy_tank_width - rocket_width
            and enemy_tank_y < rocket_y < enemy_tank_y +
            enemy_tank_height - rocket_height):
        is_fired_rocket = False
        enemy_tank_x = randint(0, screen_width - enemy_tank_width)
        enemy_tank_y = 0
        game_score += 150

game_over_text = game_font.render('Game over', True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()