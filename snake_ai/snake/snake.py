import pygame

import constants


class Snake:
    def __init__(self):
        """Initialize the snake at the center of the grid, moving right."""
        start_x = constants.START_X
        start_y = constants.START_Y
        snake_length = constants.SNAKE_LENGTH

        self.body = []
        for i in range (snake_length -1 , -1, (-1)):
            self.body.insert(0, (start_x - i, start_y))

        self.head_coord = pygame.Vector2(start_x, start_y)

        self.occupied = set(self.body)

        self.direction = pygame.Vector2(1, 0)
        self.next_direction = pygame.Vector2(1, 0)


    def change_direction(self, new_direction):
        """Change direction unless it is the opposite of the current one."""
        new_dir = pygame.Vector2(new_direction[0], new_direction[1])
        if new_dir != -self.direction:
            self.next_direction = new_dir

    def update(self, has_eaten):
        """Move the snake forward. If it ate, keep the tail; otherwise remove it.""" 
        self.direction = self.next_direction
        self.head_coord += self.direction
        self.occupied.add((int(self.head_coord.x), int(self.head_coord.y)))
        self.body.insert(0, (int(self.head_coord.x), int(self.head_coord.y)))
        if not has_eaten:
            tail = self.body.pop()
            self.occupied.remove(tail)

    def check_collision(self):
        """Return True if the next move hits a wall or the snake's own body.""" 
        next_coord = self.head_coord + self.next_direction
        nx, ny = int(next_coord.x), int(next_coord.y)
        out_of_bounds = not (0 <= nx < constants.COLUMNS and 0 <= ny < constants.ROWS)
        hits_self = (nx, ny) in self.occupied
        return out_of_bounds or hits_self
    
    def get_next_coord(self):
        """Return the next head position based on current direction."""
        next_coord = self.head_coord + self.next_direction
        return next_coord

    def get_head(self):
        """Return the current head position as a Vector2."""
        return self.head_coord
        
    def get_body(self):
        """Return the list of body segment positions."""
        return self.body
    
    def get_occupied(self):
        """Return the set of all cells currently occupied by the snake."""
        return self.occupied