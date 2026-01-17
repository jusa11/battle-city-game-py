from configs.config import SCREEN_WIDTH, SCREEN_HEIGHT

class RocketMovement:
    def __init__(self):
        pass

    def move(self, rocket):
        if rocket.angle in rocket.possible_shot_directions:
            rocket.possible_shot_directions[rocket.angle]()
            rocket.rect.x = rocket.x
            rocket.rect.y = rocket.y

            if (rocket.y < 0 or rocket.y > SCREEN_HEIGHT - rocket.height
                    or rocket.x < 0 or rocket.x > SCREEN_WIDTH - rocket.width):
                rocket.alive = False