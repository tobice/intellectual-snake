from pygame.locals import *

from src.utils.textUtils import *
from src.sprites.Head import *
from src.sprites.DirectionControl import *
from src.sprites.Segment import *

class IntellectualSnake:
    def __init__(self):
        self.running = True

        # Init the screen
        screenWidth = FIELD_WIDTH + 2 * FIELD_MARGIN
        screenHeight = FIELD_HEIGHT + 2 * FIELD_MARGIN
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))

        # Prepare the background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        # Init The Snake
        headX = SEGMENT_SIZE * COLUMNS / 2
        headY = SEGMENT_SIZE * ROWS / 2
        self.head = Head(headX, headY)
        self.segments = []
        for i in xrange(0, INIT_SNAKE_LENGTH):
            self.segments.append(Segment(headX - i * SEGMENT_SIZE, headY))

        # Init direction controls
        self.directionControls = \
            DirectionControl(screenWidth / 2, 10, UP), \
            DirectionControl(screenWidth / 2, FIELD_MARGIN + FIELD_HEIGHT + 10, DOWN), \
            DirectionControl(10, screenHeight / 2, LEFT), \
            DirectionControl(FIELD_MARGIN + FIELD_WIDTH + 10, screenHeight / 2, RIGHT)

        for control in self.directionControls:
            control.setLetter(self.generateNewDirectionLetter())

    def update(self, time):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.running = False
            elif event.type == KEYDOWN:
                self.handleKeyDown(event.key)

        self.head.update(time)

        if self.head.moved:
            self.segments.pop()
            self.segments.insert(0, Segment(self.head.rect.x, self.head.rect.y))

    def render(self):
        field = pygame.Surface([FIELD_WIDTH, FIELD_HEIGHT])
        field.fill((0, 0, 255))
        field.blit(self.head.image, self.head.rect)

        for segment in self.segments:
            field.blit(segment.image, segment.rect)

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(field, (FIELD_MARGIN, FIELD_MARGIN))

        for control in self.directionControls:
            self.screen.blit(control.image, control.rect)

    def isRunning(self):
        return self.running

    def handleKeyDown(self, key):
        # Find direction control matching the pressed letter. If found, change the snake's
        # direction according to the control and
        control = self.findControlByLetter(pygame.key.name(key))
        if control:
            if self.head.changeDirection(control.direction):
                control.setLetter(self.generateNewDirectionLetter())

    def generateNewDirectionLetter(self):
        letter = getRandomLetter()

        # The new letter must be different from the previous one and must be unique across all
        # direction letters (to avoid ambiguity)
        while len(filter(lambda control: control.letter == letter, self.directionControls)) > 0:
            letter = getRandomLetter()

        return letter

    def findControlByLetter(self, letter):
        controls = [control for control in self.directionControls if control.letter == letter]
        if not controls:
            return False
        else:
            return controls[0]
