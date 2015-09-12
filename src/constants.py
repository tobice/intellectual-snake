import assets

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

# Obstacle & bonus word rates
# (how frequently they appear on average during one second)
OBSTACLE_RATE = 0.05
BONUS_WORD_RATE = 0.2

# Colors
BACKGROUND_COLOR = (19, 72, 101)
FIELD_COLOR = (26, 210, 250)
SNAKE_COLOR = (82, 165, 115)
FOOD_COLOR = (218, 110, 67)
OBSTACLE_COLOR = (194, 47, 63)
OBSTACLE_LETTER_COLOR = (255, 255, 255)
OBSTACLE_TYPED_LETTER_COLOR = SNAKE_COLOR
HUD_COLOR = (255, 255, 255)
DIRECTION_CONTROL_COLOR = BACKGROUND_COLOR
WHITE = (255, 255, 255)

# Font
FONT = assets.path("RobotoCondensed-Bold.ttf")
FONT_SIZE = SEGMENT_SIZE

# Inner mechanics constants
HORIZONTAL = True
VERTICAL = False

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

