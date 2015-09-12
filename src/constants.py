# Game field dimensions and layout
SEGMENT_SIZE = 20
ROWS = 20
COLUMNS = 30
FIELD_WIDTH = SEGMENT_SIZE * COLUMNS
FIELD_HEIGHT = SEGMENT_SIZE * ROWS
FIELD_MARGIN = 40

# Snake length & speed
INIT_SNAKE_LENGTH = 10
STEP_DURATION = 0.1

# Colors
SNAKE_COLOR = (255, 0, 0)
FOOD_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (0, 255, 255)
WHITE = (255, 255, 255)

# How many obstacles appears per second on average
OBSTACLE_RATE = 0.3

# Inner mechanics constants
HORIZONTAL = True
VERTICAL = False

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

