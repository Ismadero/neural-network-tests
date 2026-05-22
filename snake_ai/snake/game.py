import pygame
import numpy as np

import constants
import screen
import snake as snakelib
import food as foodlib
import score as scorelib

class Game:
    def __init__(self, render = True):
        """Initialize pygame, the screen, score, food, and snake."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.timer = 0.0
        self.running = True
        self.score = scorelib.Score()
        self.render = render
        self.steps = 0
        if self.render:
            self.screen = screen.Screen()


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
                self.snake.change_direction(1)
            if keys[pygame.K_DOWN]:
                self.snake.change_direction(3)
            if keys[pygame.K_LEFT]:
                self.snake.change_direction(2)
            if keys[pygame.K_RIGHT]:
                self.snake.change_direction(0)

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

                if self.render:
                    self.screen.update(self.snake.get_occupied(), self.snake.get_head(), self.food.get_foods())
                self.timer -= constants.MOVE_INTERVAL
                self.steps += 1

    def step(self, action):
        """ Run one iteration of the game, it should not be used whit run at the same time
        action = -1 turn left
        action = 0 keep forward
        action = 1 turn right 
        
        Returns (state, reward, done)"""
        direction = self.snake.get_direction()
        self.snake.change_direction((direction - action) % 4)

        can_continue = not self.snake.check_collision()
        if not can_continue:
            self.running = False
            return self.get_state(), -10, True

        next_coord = self.snake.get_next_coord()
        next_coord = (int(next_coord.x), int(next_coord.y))
        has_eaten = self.food.eat_food(next_coord)
        self.snake.update(has_eaten)

        reward = -0.1

        if has_eaten:
            occupied_aux = self.snake.get_occupied()
            self.food.new_food(occupied_aux, 1)
            self.score.add_point()
            reward = 10

        if self.render:
            self.screen.update(self.snake.get_occupied(), self.snake.get_head(), self.food.get_foods())

        self.steps += 1
        return self.get_state(), reward, False

    def get_state(self):
        """ Return the board as a (3, ROWS, COLUMS) float32 tensor
        
        Channel 0: snake body
        
        Channel 1: snake head
        
        Channel 2: food"""
        state = np.zeros((3, constants.ROWS, constants.COLUMNS), dtype=np.float32)
        body = self.snake.get_occupied()
        for occ in body:
            state[0][occ[1]][occ[0]] = 1.0
        head = self.snake.get_head()
        state[1][int(head.y)][int(head.x)] = 1.0
        foods = self.food.get_foods()
        for food in foods:
            state[2][food[1]][food[0]] = 1.0
        return state

    def get_steps(self):
        """Returns the amouns of steps made in game"""
        return self.steps

    def quit(self):
        """Shut down pygame and return (score, max_achievable, time_seconds)."""
        time = pygame.time.get_ticks() / 1000
        pygame.quit()
        final_score = self.score.get_score()
        achievable_score = self.score.max_achievable()
        return (final_score, achievable_score, time)
