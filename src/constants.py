import os
import sys

# Game field dimensions and layout
SEGMENT_SIZE = 25
ROWS = 20
COLUMNS = 30
FIELD_WIDTH = SEGMENT_SIZE * COLUMNS
FIELD_HEIGHT = SEGMENT_SIZE * ROWS
FIELD_MARGIN = 40

# Snake length & speed
INIT_SNAKE_LENGTH = 10
STEP_DURATION = 0.1

# Colors
BACKGROUND_COLOR = (35, 40, 64)
FIELD_COLOR = (242, 236, 223)
SNAKE_COLOR = (82, 165, 115)
FOOD_COLOR = (218, 110, 67)
OBSTACLE_COLOR = (194, 47, 63)
OBSTACLE_LETTER_COLOR = (255, 255, 255)
OBSTACLE_TYPED_LETTER_COLOR = SNAKE_COLOR
HUD_COLOR = (255, 255, 255)
DIRECTION_CONTROL_COLOR = BACKGROUND_COLOR
WHITE = (255, 255, 255)

# Font
FONT = os.path.dirname(sys.argv[0]) + "/../assets/RobotoCondensed-Bold.ttf"
FONT_SIZE = SEGMENT_SIZE

# How many obstacles appears per second on average
OBSTACLE_RATE = 0.3
BONUS_WORD_RATE = 1

# Inner mechanics constants
HORIZONTAL = True
VERTICAL = False

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

