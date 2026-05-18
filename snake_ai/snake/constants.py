""" Defines the general size of the game """
SCALE = 3

""" Form of the grid """
ROWS = 15
COLUMNS = 15

TOTAL_CELLS = ROWS*COLUMNS

""" Margin outside the grid """
BORDER = 5

""" Size of the grid"""
CELLS_SIZE = 10 * SCALE 
SCREEN_SIZE = (CELLS_SIZE * COLUMNS + BORDER *2, CELLS_SIZE * ROWS + BORDER * 2)

""" Initial snake length """
SNAKE_LENGTH = 3

""" Different sizes in game """
HEAD_SIZE = 4 * SCALE
BODY_SIZE = 3 * SCALE
FOOD_SIZE = 4 * SCALE

""" Initial place for the snake """
START_X = COLUMNS//2 - 1
START_Y = ROWS//2 - 1

""" Interval for updates in state of game """
MOVE_INTERVAL = 0.175

""" Amount of food in game"""
FOOD_AMOUNT = 1

""" Colors """
BODY_COLOR = "darkgreen"
HEAD_COLOR = "green"
BACKGROUND_COLOR = "darkgray"
FOOD_COLOR = "red"

