import pygame

import constants
import screen
import snake as snakelib
import food as foodlib
import score as scorelib

class Game:
    def __init__(self):
        """Initialize pygame, the screen, score, food, and snake."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.timer = 0.0
        self.running = True
        self.screen = screen.Screen()
        self.score = scorelib.Score()


        occupied_aux = set()
        for i in range (0, constants.SNAKE_LENGTH, 1):
            occupied_aux.add((constants.START_X - i, constants.START_Y))
            
        self.food = foodlib.Food(occupied_aux, constants.FOOD_AMOUNT)

        self.snake = snakelib.Snake()

    def run(self):
        """Run the main game loop until the player loses or closes the window."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.snake.change_direction((0,-1))
            if keys[pygame.K_DOWN]:
                self.snake.change_direction((0,1))
            if keys[pygame.K_LEFT]:
                self.snake.change_direction((-1,0))
            if keys[pygame.K_RIGHT]:
                self.snake.change_direction((1,0))

            dt = self.clock.tick(60) / 1000.0
            self.timer += dt
            while self.timer >= constants.MOVE_INTERVAL:
                can_continue = not self.snake.check_collision()

                if not can_continue:
                    self.running = False

                next_coord = self.snake.get_next_coord()
                next_coord = (int(next_coord.x), int(next_coord.y))
                has_eaten = self.food.eat_food(next_coord)

                self.snake.update(has_eaten)

                if has_eaten:
                    occupied_aux = self.snake.get_occupied()
                    self.food.new_food(occupied_aux, 1)
                    self.score.add_point()

                self.screen.update(self.snake.get_occupied(), self.snake.get_head(), self.food.get_foods())
                self.timer -= constants.MOVE_INTERVAL

    def quit(self):
        """Shut down pygame and return (score, max_achievable, time_seconds)."""
        time = pygame.time.get_ticks() / 1000
        pygame.quit()
        final_score = self.score.get_score()
        achievable_score = self.score.max_achievable()
        return (final_score, achievable_score, time)