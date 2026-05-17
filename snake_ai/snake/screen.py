import pygame

import constants

class Screen:
    def __init__(self):
        """Set up the pygame display window."""
        self.screen = pygame.display.set_mode(constants.SCREEN_SIZE)
        pygame.display.flip()

    def update(self, snake_occupied, snake_head, foods):
        """Clear the screen and redraw the grid, snake, and food."""

        
        # Background color
        self.screen.fill(constants.BACKGROUND_COLOR)
 
        # This loop draws all the vertical lines for the grid
        for x in range(0, constants.COLUMNS + 1, 1):
            init_x = x*constants.CELLS_SIZE + constants.BORDER
            init_y = constants.BORDER
            
            end_x = x*constants.CELLS_SIZE + constants.BORDER
            end_y = constants.ROWS * constants.CELLS_SIZE + constants.BORDER

            pygame.draw.line(self.screen, "white", (init_x, init_y), (end_x, end_y))

        # This loop draws all the horizontal lines for the grid
        for y in range(0, constants.ROWS + 1, 1):

            init_x = constants.BORDER
            init_y = y*constants.CELLS_SIZE + constants.BORDER
            
            end_x = constants.COLUMNS * constants.CELLS_SIZE + constants.BORDER
            end_y = y*constants.CELLS_SIZE + constants.BORDER

            pygame.draw.line(self.screen, "white", (init_x, init_y), (end_x, end_y))

        # Draw the snake        
        for elem in snake_occupied:
            if elem == (int(snake_head.x), int(snake_head.y)):
                color = constants.HEAD_COLOR
                size = constants.HEAD_SIZE
            else:
                color = constants.BODY_COLOR
                size = constants.BODY_SIZE

            pixel = coord_to_pixel(elem)
            pygame.draw.circle(self.screen, color, pixel, size)
        
        # Draw the foods
        for elem in foods:
            pixel = coord_to_pixel(elem)
            pygame.draw.circle(self.screen, constants.FOOD_COLOR, pixel, constants.FOOD_SIZE)

        # Update the full new screen into the real screen
        pygame.display.flip()

def pixel_to_coord(pos):
    """Convert a pixel position to grid coordinates."""
    pos = pygame.Vector2(pos)
    x_pix = pos.x
    y_pix = pos.y
    x_coord = (x_pix - constants.CELLS_SIZE/2 - constants.BORDER)//constants.CELLS_SIZE
    y_coord = (y_pix - constants.CELLS_SIZE/2 - constants.BORDER)//constants.CELLS_SIZE
    return (x_coord, y_coord)

def coord_to_pixel(pos):
    """Convert grid coordinates to the center pixel of that cell."""
    x_coord = pos[0]
    y_coord = pos[1]
    x_pix = x_coord * constants.CELLS_SIZE + constants.CELLS_SIZE/2 + constants.BORDER
    y_pix = y_coord * constants.CELLS_SIZE + constants.CELLS_SIZE/2 + constants.BORDER
    return pygame.Vector2(x_pix, y_pix)